#!/usr/bin/env bash
# Step 1: initialise the Certification Authority (root key + self-signed cert)
set -euo pipefail
source "$(dirname "$0")/config.sh"

[ -f "$CA_DIR/ca.key" ] && { echo "CA already exists in $CA_DIR"; exit 1; }

mkdir -p "$CA_DIR"/{newcerts,crl} "$USERS_DIR"
touch "$CA_DIR/index.txt"
echo 1000 > "$CA_DIR/serial"
echo 1000 > "$CA_DIR/crlnumber"

# Minimal OpenSSL config used by 'openssl ca'
cat > "$CA_DIR/openssl.cnf" <<CNF
[ ca ]
default_ca = CA_default

[ CA_default ]
dir               = $CA_DIR
database          = \$dir/index.txt
new_certs_dir     = \$dir/newcerts
serial            = \$dir/serial
crlnumber         = \$dir/crlnumber
certificate       = \$dir/ca.crt
private_key       = \$dir/ca.key
default_md        = sha256
default_days      = $USER_DAYS
default_crl_days  = 30
policy            = policy_any
unique_subject    = no
copy_extensions   = none

[ policy_any ]
commonName        = supplied
organizationName  = optional
countryName       = optional

[ v3_ca ]
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints       = critical, CA:true
keyUsage               = critical, keyCertSign, cRLSign

[ v3_user ]
basicConstraints       = CA:false
keyUsage               = critical, digitalSignature, nonRepudiation
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid,issuer
CNF

# CA private key: RSA 4096, encrypted with a passphrase
echo ">> Generating CA private key ($CA_KEY_BITS bits)..."
openssl genrsa -aes256 ${CA_PASS:+-passout env:CA_PASS} -out "$CA_DIR/ca.key" "$CA_KEY_BITS"
chmod 400 "$CA_DIR/ca.key"

# Self-signed root certificate, 10 years
echo ">> Creating self-signed CA certificate ($CA_DAYS days)..."
openssl req -x509 -new -sha256 -key "$CA_DIR/ca.key" -days "$CA_DAYS" \
  ${CA_PASS:+-passin env:CA_PASS} -subj "$CA_SUBJECT" -config "$CA_DIR/openssl.cnf" -extensions v3_ca \
  -out "$CA_DIR/ca.crt"

openssl x509 -in "$CA_DIR/ca.crt" -noout -subject -dates
echo "CA ready."
