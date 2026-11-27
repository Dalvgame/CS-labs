#!/usr/bin/env bash
# Step 4: sign a file (RSA + SHA-256). Output: <file>.sig
# Usage: ./04_sign.sh <username> <file>
set -euo pipefail
source "$(dirname "$0")/config.sh"
USER_NAME="${1:?Usage: $0 <username> <file>}"
FILE="${2:?Usage: $0 <username> <file>}"
KEY="$USERS_DIR/$USER_NAME/$USER_NAME.key"
[ -f "$KEY" ] || { echo "No key for $USER_NAME"; exit 1; }

openssl dgst -sha256 -sign "$KEY" -out "$FILE.sig" "$FILE"
echo "Signature written to $FILE.sig"
