import nmap

ip_domain=input("Enter IP or Domain:")
print(ip_domain)

common_ports={
21 :["FTP",1],
22 :["SSH",1],
23 : ["Telnet",1],
25 : ["SMTP",0],
53 : ["DNS",0],
80 : ["HTTP",0],
443 : ["HTTPS",0],
445:["SMB",1],
3306 : ["MySQL",0],
3389 : ["RDP",1],
}
print(common_ports)

scanner=nmap.PortScanner()
ports = ",".join(str(port) for port in common_ports.keys())
state = scanner.scan(hosts=ip_domain, arguments=f"-p {ports}")
print(state)