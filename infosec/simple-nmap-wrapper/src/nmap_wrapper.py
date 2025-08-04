#!/usr/bin/env python3
import subprocess, xml.etree.ElementTree as ET, sys, socket, tabulate

def scan(target: str):
    cmd = ["nmap", "-sS", "-oX", "-", target]
    xml_out = subprocess.check_output(cmd, text=True)
    root = ET.fromstring(xml_out)
    rows = []
    for host in root.findall("host"):
        ip = host.find("address").attrib["addr"]
        for port in host.findall("./ports/port"):
            state = port.find("state").attrib["state"]
            svc = port.find("service").attrib.get("name", "")
            rows.append([ip, port.attrib["portid"], state, svc])
    print(tabulate.tabulate(rows, headers=["IP", "PORT", "STATE", "SERVICE"]))

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "scanme.nmap.org"
    scan(target)