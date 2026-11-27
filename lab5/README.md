# Lab 5 – Internal PKI with OpenSSL (Bash)

Requirements: Linux/macOS/WSL/Git-Bash with OpenSSL.  Run `chmod +x *.sh` once.

| Step | Command | What it does |
|------|---------|--------------|
| 1 | `./01_init_ca.sh` | RSA-4096 CA key + self-signed cert (3650 days) |
| 2 | `./02_issue_user.sh alice` | RSA-2048 user key, CSR, cert signed by CA (365 days) |
| 3 | `./03_revoke_user.sh alice` | Revokes the cert, regenerates the CRL |
| 4 | `./04_sign.sh alice file.txt` | Signs the file (RSA + SHA-256) -> `file.txt.sig` |
| 5 | `./05_verify.sh alice file.txt` | Checks cert (chain/expiry/CRL), then the signature |

The CA key is protected by a passphrase; OpenSSL asks for it in steps 1-3.
For automation you can `export CA_PASS=yourpass` first.

Outputs live in `pki-data/` (`ca/` and `users/<name>/`).

Quick demo:
    ./01_init_ca.sh
    ./02_issue_user.sh alice
    echo "hello" > doc.txt
    ./04_sign.sh alice doc.txt
    ./05_verify.sh alice doc.txt      # SIGNATURE VALID
    ./03_revoke_user.sh alice
    ./05_verify.sh alice doc.txt      # INVALID: certificate revoked
