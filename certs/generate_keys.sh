#!/bin/bash

OPENSSL=~/oqs-openssl/apps/openssl
CONF_FILE=openssl-oqs.cnf

echo "[+] Generating RSA + Kyber Level 1 hybrid cert..."
$OPENSSL req -new -newkey rsa:3072 -keyout rsa_kyber.key -nodes -subj "/CN=localhost" -config $CONF_FILE -out rsa_kyber.csr
$OPENSSL x509 -req -in rsa_kyber.csr -out rsa_kyber.crt -days 365 -extfile $CONF_FILE -extensions v3_ca -key rsa_kyber.key

echo "[+] Generating ECDSA + Dilithium Level 3 hybrid cert..."
$OPENSSL req -new -newkey ec:<(echo "prime256v1") -keyout ecdsa_dilithium.key -nodes -subj "/CN=localhost" -config $CONF_FILE -out ecdsa_dilithium.csr
$OPENSSL x509 -req -in ecdsa_dilithium.csr -out ecdsa_dilithium.crt -days 365 -extfile $CONF_FILE -extensions v3_ca -key ecdsa_dilithium.key

echo "[✔] Hybrid certificates generated successfully."
