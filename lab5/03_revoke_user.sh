#!/usr/bin/env bash
# Step 3: revoke a user's certificate and regenerate the CRL
# Usage: ./03_revoke_user.sh <username>
set -euo pipefail
source "$(dirname "$0")/config.sh"
USER_NAME="${1:?Usage: $0 <username>}"
CRT="$USERS_DIR/$USER_NAME/$USER_NAME.crt"
[ -f "$CRT" ] || { echo "No certificate for $USER_NAME"; exit 1; }

PASS_OPT=${CA_PASS:+-passin env:CA_PASS}
openssl ca -config "$CA_DIR/openssl.cnf" -revoke "$CRT" $PASS_OPT
openssl ca -config "$CA_DIR/openssl.cnf" -gencrl -out "$CA_DIR/crl/ca.crl" $PASS_OPT
echo "Certificate of $USER_NAME revoked. CRL updated: $CA_DIR/crl/ca.crl"
