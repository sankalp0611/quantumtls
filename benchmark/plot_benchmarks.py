import pandas as pd
import matplotlib.pyplot as plt

# Load the benchmark results
df = pd.read_csv("results.csv")

# Filter out RSA if it failed (avg time = 0 or cipher unknown)
df = df[df["AvgHandshakeTime(ms)"] > 0]

# Plot 1: Handshake Time
plt.figure(figsize=(8, 5))
plt.bar(df["Mode"], df["AvgHandshakeTime(ms)"], color=["#ff6666", "#66b3ff"])
plt.title("TLS Handshake Time (ms)")
plt.ylabel("Avg Time (ms)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("graphs/handshake_time.png")
print("[✅] handshake_time.png saved!")

# Plot 2: Certificate Size
plt.figure(figsize=(8, 5))
plt.bar(df["Mode"], df["CertSize(Bytes)"], color=["#ffcc99", "#99ff99"])
plt.title("Certificate Size (Bytes)")
plt.ylabel("Size (Bytes)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("graphs/cert_size.png")
print("[✅] cert_size.png saved!")
