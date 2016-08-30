# PyVault

Yet another implementation of Vault using pure Python (json and gnupg modules). This has nothing to do with Vault provided by Hashicorp. This is also not supposed nor recommended to use in any production environment.

## Installation

The easiest way is to use [this](https://copr.fedorainfracloud.org/coprs/fkolacek/PyVault/) COPR repository and then just use dnf:

~~~
# dnf copr enable fkolacek/PyVault
# dnf install PyVault Pyvault-utils
~~~

## Usage:

First of all you should initialize your vault using:
~~~
$ pyvault init
~~~

if you want to create/write new entry just use:
~~~
$ pyvault write <key> <value>
~~~

for reading use:
```
$ pyvault read <key>
```
for deleting old entries use:
```
$ pyvault delete <key>
```

it is also possible to dump all passwords:
```
$ pyvault dump
```

or using read:
~~~
$ pyvault read / | jq
~~~

## TODO
 - Implement interactive shell
 - Create GUI client

## Features
 - Bash autocompletion for commands
 - Using PGP encryption as backend
 - Written in pure Python (no external dependencies)
 - Data integrity checking (cannot override data by accident)

## Working example
```
0 ✓ 0s ~$ pyvault init
[*] Vault .vaultdb does not exist, creating one.
0 ✓ 0s ~$ pyvault write /servers/production/saber.example.com/root password1
0 ✓ 0s ~$ pyvault write /servers/production/shiny.example.com/root password2
0 ✓ 0s ~$ pyvault write /servers/stage/kenny.example.com/root password3
0 ✓ 0s ~$ pyvault write /servers/stage/kenny.example.com/mysql password4
0 ✓ 0s ~$ pyvault write /servers/stage/lenny.example.com password5
0 ✓ 0s ~$ pyvault write /servers/nas.home.example.com/root password6
0 ✓ 0s ~$ pyvault write '/services/teampass/fkolacek@redhat.com' password7
0 ✓ 0s ~$ pyvault write '/services/lastpass/fkolacek@redhat.com' password8

0 ✓ 0s ~$ cat .vaultdb
-----BEGIN PGP MESSAGE-----
Version: GnuPG v1

jA0EBwMCRsQUxljBIyNg0sAeAQmIxQ01+jPoratIC9byYJ/HL134Xftz0wC/7O3O
oONGtzI6/xWvQdt0zYva1L9GeYRUWaRl06XnMZ9b8gU8vt1ztFP+kCBQ629pzcS2
33OMVWy+UmEI9HAUZRS+W4NZuYJojRTsACvJaNB89nk2hy6ghgrEtzfoC5Bvamja
wMex5Qx0MZEsELxv8hx24IoH7RxFvPul+6aJ7UizjgneUGJaGVXFccjeZSLkC5OX
fPQ72DqUcaFv0K3qvQJkcu2lhg2qR/ZcNW16pKBV0nw6lJHI1SybncAEJ17iRFoz
=ivLc
-----END PGP MESSAGE-----

0 ✓ 0s ~$ pyvault dump
/service/lastpass/fkolacek@redhat.com password8
/service/teampass/fkolacek@redhat.com password7
/servers/production/saber.example.com/root password1
/servers/production/shiny.example.com/root password2
/servers/nas.home.example.com/root password6
/servers/stage/lenny.example.com password5
/servers/stage/kenny.example.com/root password3
/servers/stage/kenny.example.com/mysql password4

0 ✓ 0s ~$ pyvault read /servers/production/saber.example.com/root
password1
0 ✓ 0s ~$ pyvault read /servers/stage/kenny.example.com
{'root': 'password3', 'mysql': 'password4'}

0 ✓ 0s ~$ pyvault read / | python -mjson.tool
{
    "servers": {
        "nas.home.example.com": {
            "root": "password6"
        },
        "production": {
            "saber.example.com": {
                "root": "password1"
            },
            "shiny.example.com": {
                "root": "password2"
            }
        },
        "stage": {
            "kenny.example.com": {
                "mysql": "password4",
                "root": "password3"
            },
            "lenny.example.com": "password5"
        }
    },
    "services": {
        "lastpass": {
            "fkolacek@redhat.com": "password8"
        },
        "teampass": {
            "fkolacek@redhat.com": "password7"
        }
    }
}

0 ✓ 0s ~$ pyvault read /404
2 ✗ 0s ~$ pyvault read /servers/
[!] Entry name must not end with /
2 ✗ 0s ~$ pyvault write /servers password9
[!] Entry /servers already exists, delete it first
0 ✓ 0s ~$ pyvault write /servers/nas.home.example.com password9
[!] Entry /servers/nas.home.example.com already exists, delete it first
```
## License

Released under GNU / GPL, for more info see LICENSE file.

## Author

Frantisek Kolacek (<fkolacek@redhat.com>)
