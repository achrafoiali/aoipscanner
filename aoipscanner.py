import socket
import os

RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

os.system("clear" if os.name != "nt" else "cls")

print(f"""{RED}
 █████╗  ██████╗ 
██╔══██╗██╔═══██╗
███████║██║   ██║
██╔══██║██║   ██║
██║  ██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝

██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║██║         ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                    ⚡ AO IP SCANNER ⚡
{RESET}""")

ip = input(f"{RED}Enter IP: {WHITE}")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]

print(f"\n{RED}Scanning {ip}...{RESET}\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    if sock.connect_ex((ip, port)) == 0:
        print(f"{RED}[+] Port {port} OPEN{RESET}")
    else:
        print(f"{WHITE}[-] Port {port} CLOSED{RESET}")

    sock.close()

print(f"\n{RED}AO IP SCANNER — Scan completed.{RESET}")
