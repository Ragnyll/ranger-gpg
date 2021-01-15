# ranger-gpg
&nbsp;&nbsp;&nbsp;&nbsp;Ranger functions for encrypting and decrypting files and directories using gpg keys.

## Requirements
&nbsp;&nbsp;&nbsp;&nbsp;A `default-key` conf option must be set in `~/.gnupg/gpg.conf` in order to state what public key to encrypt with.

Ex: `~/.gnupg/gpg.conf`

```
default-key PGP_PUBLIC_KEY_ID
```

## Installation
```
git clone https://gitlab.com/Ragnyll/ranger-gpg.git
cd ranger-gpg
make install
```

## Uninstall
```
make uninstall
```
