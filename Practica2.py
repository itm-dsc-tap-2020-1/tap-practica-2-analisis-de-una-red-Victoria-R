import os
red ="200.33.171.0/24"
os.system("nmap -sP " + red)
"""Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 12:01 CST
Stats: 0:00:00 elapsed; 0 hosts completed (0 up), 256 undergoing Ping Scan
Ping Scan Timing: About 1.27% done; ETC: 12:01 (0:00:00 remaining)
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.0051s latency).
Nmap scan report for 200.33.171.13
Host is up (0.024s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.0080s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.0087s latency).
Nmap scan report for 200.33.171.85
Host is up (0.0080s latency).
Nmap scan report for 200.33.171.99
Host is up (0.013s latency).
Nmap scan report for 200.33.171.115
Host is up (0.0048s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.0091s latency).
Nmap scan report for 200.33.171.125
Host is up (0.0076s latency).
Nmap done: 256 IP addresses (9 hosts up) scanned in 4.34 seconds"""