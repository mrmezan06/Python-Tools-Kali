import socket
from IPy import IP

class PortScan():

    banners = []
    open_ports = []
    def __init__(self, target, port):
        self.target = target
        self.port = port

    def scan(self):    
        for p in range(1,self.port):
            self.scan_port(p)

    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass

# Facebook.com : 157.240.235.35
# if __name__ == "__main__":
#     targets = input('[+] Enter target/s to scan(split multiple targets with comma(,)): ')
#     if ',' in targets:
#         for ip_add in targets.split(','):
#             scan(ip_add.strip(' '))
#     else:
#         scan(targets)
#converted_ip = check_ip(ipaddress)

