import requests

res = requests.get("https://localhost:4433", verify="server_cert.pem")
print("🔐 TLS Handshake Success!")
print(res.text)
