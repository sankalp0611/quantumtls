# QuantumTLS — Hybrid Post-Quantum TLS Certificate Generator

This project integrates [Open Quantum Safe](https://openquantumsafe.org) with OpenSSL to generate hybrid TLS certificates using quantum-safe algorithms like Kyber and Dilithium, alongside traditional RSA/ECDSA.

## 🔐 Features
- RSA + Kyber Level 1 Certificate
- ECDSA + Dilithium Level 3 Certificate
- Fully automated with `generate_keys.sh`
- Backup support with `backup_certs.sh`

## 📁 Structure
certs/
├── generate_keys.sh
├── backup_certs.sh
├── openssl-oqs.cnf
├── rsa_kyber.crt/.key/.csr
├── ecdsa_dilithium.crt/.key/.csr
