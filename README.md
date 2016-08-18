Vault

Usage:
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/production/saber.example.com/root password1
[*] Vault /home/fkolacek/vault.db does not exist, creating one.
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/production/shiny.example.com/root password2
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/stage/kenny.example.com/root password3
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/stage/kenny.example.com/mysql password4
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/stage/lenny.example.com password5
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/nas.home.example.com/root password6
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db '/services/teampass/fkolacek@redhat.com' password7
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db '/services/lastpass/fkolacek@redhat.com' password8
0 ✓ 0s fkolacek@carby ~ $ cat ~/vault.db | python -mjson.tool
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
0 ✓ 0s fkolacek@carby ~ $ vault.py read ~/vault.db /servers/production/saber.example.com/root
password1
0 ✓ 0s fkolacek@carby ~ $ vault.py read ~/vault.db /servers/stage/kenny.example.com
{u'root': u'password3', u'mysql': u'password4'}
0 ✓ 0s fkolacek@carby ~ $ vault.py read ~/vault.db /
{u'services': {u'lastpass': {u'fkolacek@redhat.com': u'password8'}, u'teampass': {u'fkolacek@redhat.com': u'password7'}}, u'servers': {u'production': {u'saber.example.com': {u'root': u'password1'}, u'shiny.example.com': {u'root': u'password2'}}, u'nas.home.example.com': {u'root': u'password6'}, u'stage': {u'lenny.example.com': u'password5', u'kenny.example.com': {u'root': u'password3', u'mysql': u'password4'}}}}
0 ✓ 0s fkolacek@carby ~ $ vault.py read ~/vault.db /404
2 ✗ 0s fkolacek@carby ~ $ vault.py read ~/vault.db /servers/
[!] Invalid key (should not end with /)
2 ✗ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers password9
0 ✓ 0s fkolacek@carby ~ $ vault.py write ~/vault.db /servers/nas.home.example.com password9
[!] Entry /servers already exists, delete it first!

