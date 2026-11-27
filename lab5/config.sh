#!/usr/bin/env bash
# Shared settings for the internal PKI
PKI_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/pki-data"
CA_DIR="$PKI_DIR/ca"
USERS_DIR="$PKI_DIR/users"
CA_KEY_BITS=4096
CA_DAYS=3650
USER_KEY_BITS=2048
USER_DAYS=365
CA_SUBJECT="/C=MD/O=Lab PKI/CN=Lab Root CA"
