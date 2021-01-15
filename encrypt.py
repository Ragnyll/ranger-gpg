import os
import tarfile
from gnupg import GPG
from ranger.api.commands import Command
from subprocess import run


class encrypt(Command):
    """:encrypt

    Encrypts a file or dir (as a tar.gz) with the default gpg key
    """

    def tardir(self, path):
        """:tardir

        tars a directory into a dir of the same name appended with .tar.gz

        returns the name of the tarfile
        """
        output_path = path + '.tar.gz'

        with tarfile.open(output_path, "w:gz") as tar_handle:
            for root, dirs, files in os.walk(path):
                for file in files:
                    tar_handle.add(os.path.join(root, file))

        return output_path

    def get_default_pub_key(self, gpg_home):
        """

        returns False if the default_key was not found
        """
        with open(os.path.join(gpg_home, 'gpg.conf'), 'r') as gpg_conf:
            line = [line for line in gpg_conf.readlines() if 'default-key' in line]
            if not line:
                return False

        return line[0].split(' ')[1][:-1]

    def execute(self):
        gpg_home = os.path.join(os.path.expanduser('~'), '.gnupg/')
        default_key = self.get_default_pub_key(gpg_home)

        if not default_key:
            self.fm.notify('default-key configuration could not be found in ~/.gnupg/gpg.conf')
            return

        gpg = GPG(gpgbinary='/usr/bin/gpg', gnupghome=gpg_home)

        paths = [os.path.basename(f.path) for f in self.fm.thistab.get_selection()]

        for p in paths:
            if os.path.isdir(p):
                new_p = self.tardir(p)
                run(['rm', '-rf', p])
                p = new_p

            with open(p, 'rb') as f:
                enc = gpg.encrypt_file(f, default_key)

            with open(p + '.gpg', 'wb+') as out:
                out.write(enc.data)

            if os.path.isfile(p):
                os.remove(p)
