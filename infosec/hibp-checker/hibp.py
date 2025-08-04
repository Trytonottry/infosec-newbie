#!/usr/bin/env python3
import requests, sys, hashlib, getpass

def check(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": sys.getenv("HIBP_KEY")}
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        print("Breaches:", [b["Name"] for b in r.json()])
    else:
        print("Clean or API error")

if __name__ == "__main__":
    email = sys.argv[1] if len(sys.argv) > 1 else input("Email: ")
    check(email)