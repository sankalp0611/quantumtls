#!/bin/bash

export OPENSSL_CONF=$HOME/quantumtls/openssl.cnf
export OPENSSL_MODULES=$HOME/oqs-provider/build/lib

CERT=$1
KEY=$2
DESC=$3

echo "🚀 Testing $DESC..."

openssl s_server \
  -accept 4433 \
  -cert $CERT \
  -key $KEY \
  -provider default \
  -provider oqsprovider \
  -ciphersuites TLS_AES_256_GCM_SHA384 \
  -www &

PID=$!
sleep 1

openssl s_client \
  -connect localhost:4433 \
  -provider default \
  -provider oqsprovider \
  -ciphersuites TLS_AES_256_GCM_SHA384 \
  -msg -debug > logs/handshake_${DESC}.log

kill $PID
