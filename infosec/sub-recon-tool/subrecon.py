#!/usr/bin/env python3
import subprocess, sys, socket

def run(cmd):
    return subprocess.check_output(cmd, text=True).splitlines()

def main(domain):
    subs = set()
    for tool in [["subfinder", "-silent", "-d", domain],
                 ["amass", "enum", "-passive", "-d", domain]]:
        subs.update(run(tool))
    for s in sorted(subs):
        try:
            ip = socket.gethostbyname(s)
            print(f"{s} {ip}")
        except:
            print(f"{s} NXDOMAIN")

if __name__ == "__main__":
    main(sys.argv[1])