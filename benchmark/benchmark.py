import subprocess
import time
import os
import csv

CERT_DIR = "certs"
LOG_DIR = "logs"
RESULT_FILE = "results.csv"
ROUNDS = 5
PORT = 4443

MODES = {
    "RSA": {
        "cert": "rsa_cert.pem",
        "key": "rsa.key"
    },
    "PQC": {
        "cert": "pqc_cert.pem",
        "key": "pqc.key"
    },
    "Hybrid": {
        "cert": "hybrid_cert.pem",
        "key": "hybrid.key"
    }
}

os.makedirs(LOG_DIR, exist_ok=True)

# Clean old results
if os.path.exists(RESULT_FILE):
    os.remove(RESULT_FILE)

# Write CSV header
with open(RESULT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Mode", "CertSize(Bytes)", "AvgHandshakeTime(ms)", "CipherSuite"])

def get_cert_size(cert_path):
    return os.path.getsize(cert_path)

def extract_cipher(log_path):
    try:
        with open(log_path, "r") as f:
            for line in f:
                if "Cipher" in line and ":" in line:
                    return line.strip().split(":")[1].strip()
    except:
        return "Unknown"
    return "Unknown"

def run_handshake(mode, cert_file, key_file):
    times = []
    cert_path = os.path.join(CERT_DIR, cert_file)
    key_path = os.path.join(CERT_DIR, key_file)
    log_path = os.path.join(LOG_DIR, f"{mode.lower()}_client.log")

    # 🔧 Fixed provider logic
    if mode == "RSA":
        provider_args = ["-provider", "default"]
    else:
        provider_args = ["-provider", "oqsprovider", "-provider-path", "/usr/local/lib"]

    for i in range(ROUNDS):
        print(f"[{mode}] Starting round {i+1}...")

        server_cmd = [
            "openssl", "s_server",
            "-quiet",
            "-accept", str(PORT),
            "-cert", cert_path,
            "-key", key_path
        ] + provider_args

        server = subprocess.Popen(server_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)

        client_cmd = [
            "openssl", "s_client",
            "-connect", f"localhost:{PORT}"
        ] + provider_args

        start = time.time()
        with open(log_path, "w") as log_file:
            try:
                subprocess.run(client_cmd, stdout=log_file, stderr=log_file, timeout=5)
            except subprocess.TimeoutExpired:
                print(f"[{mode}] ⚠️ Timeout on round {i+1}")
                server.kill()
                continue
        end = time.time()
        handshake_time = (end - start) * 1000
        times.append(handshake_time)

        server.kill()
        time.sleep(1)

    avg_time = round(sum(times) / len(times), 2) if times else 0.0
    cert_size = get_cert_size(cert_path)
    cipher = extract_cipher(log_path)

    with open(RESULT_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([mode, cert_size, avg_time, cipher])

    print(f"[✅] {mode} done: AvgTime={avg_time}ms, CertSize={cert_size}B, Cipher={cipher}\n")

# 🔁 Run all benchmark modes
for mode, paths in MODES.items():
    run_handshake(mode, paths["cert"], paths["key"])

print(f"\n[✅] All benchmarks completed. Results saved to {RESULT_FILE}")

