# PyVault

Yet another implementation of Vault using pure Python (json and gnupg modules). This has nothing to do with Vault provided by Hashicorp. This is also not supposed nor recommended to use in any production environment.

## Usage:

If you want to create/write new entry just use:
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

## TODO
 - Implement data encryption (planning to use gnupg module and symmetric encryption


## Features
 - Bash autocompletion for commands
 - Using PGP encryption as backend
 - Written in pure Python (no external dependencies)
 - Data integrity checking (cannot override data by accident)

## Working example
```
0 ✓ 0s fkolacek@carby ~ $ pyvault write /servers/production/saber.example.com/root password1
[*] Vault .vaultdb does not exist, creating one.
0 ✓ 0s fkolacek@carby ~ $ pyvault write  /servers/production/shiny.example.com/root password2
0 ✓ 0s fkolacek@carby ~ $ pyvault write  /servers/stage/kenny.example.com/root password3
0 ✓ 0s fkolacek@carby ~ $ pyvault write  /servers/stage/kenny.example.com/mysql password4
0 ✓ 0s fkolacek@carby ~ $ pyvault write  /servers/stage/lenny.example.com password5
0 ✓ 0s fkolacek@carby ~ $ pyvault write  /servers/nas.home.example.com/root password6
0 ✓ 0s fkolacek@carby ~ $ pyvault write  '/services/teampass/fkolacek@redhat.com' password7
0 ✓ 0s fkolacek@carby ~ $ pyvault write  '/services/lastpass/fkolacek@redhat.com' password8
0 ✓ 0s fkolacek@carby ~ $ cat .vaultdb | python -mjson.tool
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
0 ✓ 0s fkolacek@carby ~ $ pyvault dump
/service/lastpass/fkolacek@redhat.com password8
/service/teampass/fkolacek@redhat.com password7
/servers/production/saber.sniff.ws/root password1
/servers/production/shiny.sniff.ws/root password2
/servers/nas.home.sniff.ws/root password6
/servers/stage/lenny.sniff.ws password5
/servers/stage/kenny.sniff.ws/root password3
/servers/stage/kenny.sniff.ws/mysql password4
0 ✓ 0s fkolacek@carby ~ $ pyvault read /servers/production/saber.example.com/root
password1
0 ✓ 0s fkolacek@carby ~ $ pyvault read /servers/stage/kenny.example.com
{u'root': u'password3', u'mysql': u'password4'}
0 ✓ 0s fkolacek@carby ~ $ pyvault read /
{u'services': {u'lastpass': {u'fkolacek@redhat.com': u'password8'}, u'teampass': {u'fkolacek@redhat.com': u'password7'}}, u'servers': {u'production': {u'saber.example.com': {u'root': u'password1'}, u'shiny.example.com': {u'root': u'password2'}}, u'nas.home.example.com': {u'root': u'password6'}, u'stage': {u'lenny.example.com': u'password5', u'kenny.example.com': {u'root': u'password3', u'mysql': u'password4'}}}}
0 ✓ 0s fkolacek@carby ~ $ pyvault read /404
2 ✗ 0s fkolacek@carby ~ $ pyvault read /servers/
[!] Invalid key (should not end with /)
2 ✗ 0s fkolacek@carby ~ $ pyvault write /servers password9
0 ✓ 0s fkolacek@carby ~ $ pyvault write /servers/nas.home.example.com password9
[!] Entry /servers already exists, delete it first!

```

## Author

Frantisek Kolacek (<fkolacek@redhat.com>)
