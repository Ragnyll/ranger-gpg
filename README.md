# ranger-gpg
&nbsp;&nbsp;&nbsp;&nbsp;Ranger functions for encrypting and decrypting files and directories using gpg keys.

![ranger-gpg](assets/ex.gif)

## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;A `default-key` conf option must be set in `~/.gnupg/gpg.conf` in order to state what public key to encrypt with.

Ex: `~/.gnupg/gpg.conf`

```
default-key PGP_PUBLIC_KEY_ID
```

## Usage
**Encryption**

&nbsp;&nbsp;&nbsp;&nbsp;Call `:encrypt` to encrypt with the default-key

**Decryption**

&nbsp;&nbsp;&nbsp;&nbsp;Call `:decrypt` to decrypt with the available secret key. If the secret key is not available the command will fail

## Installation
```
git clone https://gitlab.com/Ragnyll/ranger-gpg.git
cd ranger-gpg
pip install python-gnupg
make install
```

## Uninstall
```
make uninstall
```
