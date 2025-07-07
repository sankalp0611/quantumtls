# 🔐 QuantumTLS — Post-Quantum TLS 1.3 Engine

![License](https://img.shields.io/github/license/sankalp0611/quantumtls?color=blue)
![OpenSSL + oqsprovider](https://img.shields.io/badge/Backend-OpenSSL%20%2B%20liboqs-success)
![Built With](https://img.shields.io/badge/Built%20With-Python%20%7C%20Bash%20%7C%20OpenSSL-orange)

> **QuantumTLS** is a full TLS 1.3 handshake engine supporting **Post-Quantum Cryptography (PQC)** using [liboqs](https://openquantumsafe.org/) + [oqs-provider](https://github.com/open-quantum-safe/oqs-provider).  
> It implements and benchmarks **RSA-only**, **PQC-only (Falcon512)**, and **Hybrid (RSA + Falcon512)** certificate-based TLS modes with real certs, PCAPs, and automated graphs.

---

## 📸 Preview

### ⏱️ Handshake Time

![Handshake Time](benchmark/graphs/handshake_time.png)

### 📜 Certificate Size

![Cert Size](benchmark/graphs/cert_size.png)

---

## 🧠 Features

✅ TLS 1.3 Handshakes using:
- Falcon512 PQC Signature
- RSA 3072 legacy
- Hybrid Certs (RSA + Falcon)

✅ Scripts for:
- Automated benchmarking (latency, size, cipher)
- Certificate generation
- Plotting CSV data as graphs

✅ Wireshark + PCAP Support  
✅ Interview-ready explanations & tradeoffs

---

## ⚙️ How It Works

1. Built OpenSSL with **oqs-provider** and **liboqs**
2. Generated 3 types of certs:
   - `rsa_cert.pem`, `rsa.key`
   - `pqc_cert.pem`, `pqc.key` (Falcon512)
   - `hybrid_cert.pem`, `hybrid.key` (RSA + Falcon)
3. Automated 5-round benchmarking via `benchmark.py`
4. Captured cert sizes + handshake times → CSV → graphs

