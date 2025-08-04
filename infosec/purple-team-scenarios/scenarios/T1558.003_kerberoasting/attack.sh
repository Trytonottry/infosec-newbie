#!/bin/bash
# требует impacket
python3 -m impacket.GetUserSPNs -dc-ip dc.test.local test.local/lowpriv