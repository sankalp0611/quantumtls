#!/bin/bash

BACKUP_DIR=backup

mkdir -p $BACKUP_DIR
cp *.crt *.key *.csr *.cnf $BACKUP_DIR 2>/dev/null

echo "[✔] Backup completed to $BACKUP_DIR/"

