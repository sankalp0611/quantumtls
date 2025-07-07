#!/bin/bash

# Paths
CERT_DIR="./benchmark/certs"
KEY_FILE="$CERT_DIR/pqc.key"
CERT_FILE="$CERT_DIR/pqc_cert.pem"

# Optional config (you can remove -config if not needed)
CONFIG_FILE="./certs/openssl-oqs.cnf"

echo "[*] Generating PQC key (Falcon512)..."
openssl genpkey \
    -provider oqsprovider \
    -provider-path /usr/local/lib \
    -algorithm falcon512 \
    -out "$KEY_FILE"

echo "[*] Generating self-signed PQC certificate..."
openssl req -new -x509 \
    -key "$KEY_FILE" \
    -out "$CERT_FILE" \
    -subj "/CN=PQC-Only-Cert-Falcon512" \
    -days 365 \
    -sha512 \
    -provider oqsprovider \
    -provider-path /usr/local/lib \
    -config "$CONFIG_FILE"

echo "[✅] Falcon PQC certificate generated at: $CERT_FILE"

