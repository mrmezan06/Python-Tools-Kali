import port_scanner

targets = input('[+] * Enter target to scan for vulnerabilities of open ports: ')
port = int(input('[+] * Enter amount of ports you want scan (500 - for first 500 ports) : '))
vul_file = input('[+] * Enter the path to the file with vulnerable softwares: ')
print('\n')

target = port_scanner.PortScan(targets, port)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] Vulnerable banner: ' + banner + ' On port' + str(target.open_ports[count]))
        count += 1

    