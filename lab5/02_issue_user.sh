#!/usr/bin/env bash
# Step 2: issue a key + certificate for a user (valid 365 days, RSA 2048)
# Usage: ./02_issue_user.sh <username>
set -euo pipefail
source "$(dirname "$0")/config.sh"
USER_NAME="${1:?Usage: $0 <username>}"
U="$USERS_DIR/$USER_NAME"

[ -f "$CA_DIR/ca.crt" ] || { echo "Run 01_init_ca.sh first"; exit 1; }
[ -f "$U/$USER_NAME.crt" ] && { echo "User $USER_NAME already has a certificate"; exit 1; }
mkdir -p "$U"

echo ">> Generating private key ($USER_KEY_BITS bits)..."
openssl genrsa -out "$U/$USER_NAME.key" "$USER_KEY_BITS"
chmod 400 "$U/$USER_NAME.key"

echo ">> Creating CSR..."
openssl req -new -sha256 -key "$U/$USER_NAME.key" \
  -subj "/C=MD/O=Lab PKI/CN=$USER_NAME" -out "$U/$USER_NAME.csr"

echo ">> Signing certificate with CA ($USER_DAYS days)..."
openssl ca -batch -config "$CA_DIR/openssl.cnf" -extensions v3_user \
  -days "$USER_DAYS" -notext -in "$U/$USER_NAME.csr" -out "$U/$USER_NAME.crt" \
  ${CA_PASS:+-passin env:CA_PASS}

openssl x509 -in "$U/$USER_NAME.crt" -noout -subject -serial -dates
echo "Certificate issued for $USER_NAME."
