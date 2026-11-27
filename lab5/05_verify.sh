#!/usr/bin/env bash
# Step 5: verify the signer's certificate (chain, expiry, revocation) and the signature
# Usage: ./05_verify.sh <username> <file> [signature]
set -euo pipefail
source "$(dirname "$0")/config.sh"
USER_NAME="${1:?Usage: $0 <username> <file> [signature]}"
FILE="${2:?Usage: $0 <username> <file> [signature]}"
SIG="${3:-$FILE.sig}"
CRT="$USERS_DIR/$USER_NAME/$USER_NAME.crt"

echo ">> Checking certificate (CA chain, validity, CRL)..."
CRL_ARGS=()
if [ -f "$CA_DIR/crl/ca.crl" ]; then
  CRL_ARGS=(-crl_check -CRLfile "$CA_DIR/crl/ca.crl")
fi
openssl verify -CAfile "$CA_DIR/ca.crt" "${CRL_ARGS[@]}" "$CRT" \
  || { echo "INVALID: certificate is revoked, expired or untrusted"; exit 1; }

echo ">> Verifying signature..."
openssl x509 -in "$CRT" -pubkey -noout > "$USERS_DIR/$USER_NAME/pub.tmp"
openssl dgst -sha256 -verify "$USERS_DIR/$USER_NAME/pub.tmp" -signature "$SIG" "$FILE" \
  && echo "SIGNATURE VALID" || { echo "SIGNATURE INVALID"; rm -f "$USERS_DIR/$USER_NAME/pub.tmp"; exit 1; }
rm -f "$USERS_DIR/$USER_NAME/pub.tmp"
