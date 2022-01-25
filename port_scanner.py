import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[_0 Scanning Target] ' + str(target))
    for port in range(1,500):
        scan_port(converted_ip, port)

def check_ip(ipaddress):
    try:
        IP(ipaddress)
        return ipaddress
    except ValueError:
        return socket.gethostbyname(ipaddress)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):

    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Port ' + str(port) + ' is open : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is open')
    except:
        pass

# Facebook.com : 157.240.235.35
if __name__ == "__main__":
    targets = input('[+] Enter target/s to scan(split multiple targets with comma(,)): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
#converted_ip = check_ip(ipaddress)

