import nmap
from colorama import init, Fore, Style

init()

def print_ports(title, ports_dict):
    print(f"{title}:")
    if not ports_dict:
        print(" (none)")
    else:
        for port, service in ports_dict.items():
            print(f"Port {port}: {service[0]} , Protocol: {service[1]}")
    print()

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
state = scanner.scan(hosts=ip_domain, arguments=f"-sS -sU -p T:{ports},U:{ports}")
open_ports={}
closed_ports={}
filtered_ports={}
unfiltered_ports={}
open_filtered_ports={}
closed_filtered_ports={}
for port in scanner[ip_domain]['tcp']:
    if scanner[ip_domain]['tcp'][port]['state'] == 'open':
        open_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']  
    elif scanner[ip_domain]['tcp'][port]['state'] == 'closed':    
        closed_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
    elif scanner[ip_domain]['tcp'][port]['state'] == 'filtered':
        filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
    elif scanner[ip_domain]['tcp'][port]['state'] == 'unfiltered':
        unfiltered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
    elif scanner[ip_domain]['tcp'][port]['state'] == 'open|filtered':
        open_filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']
    elif scanner[ip_domain]['tcp'][port]['state'] == 'closed|filtered':
        closed_filtered_ports[port]=[scanner[ip_domain]['tcp'][port]['name'],'tcp']


for port in scanner[ip_domain]['udp']:
    if scanner[ip_domain]['udp'][port]['state'] == 'open':
        open_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']  
    elif scanner[ip_domain]['udp'][port]['state'] == 'closed':    
        closed_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
    elif scanner[ip_domain]['udp'][port]['state'] == 'filtered':
        filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
    elif scanner[ip_domain]['udp'][port]['state'] == 'unfiltered':
        unfiltered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
    elif scanner[ip_domain]['udp'][port]['state'] == 'open|filtered':
        open_filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
    elif scanner[ip_domain]['udp'][port]['state'] == 'closed|filtered':
        closed_filtered_ports[port]=[scanner[ip_domain]['udp'][port]['name'],'udp']
     

print_ports("Open Ports", open_ports)
print_ports("Closed Ports", closed_ports)
print_ports("Filtered Ports", filtered_ports)
print_ports("Unfiltered Ports", unfiltered_ports)
print_ports("Open|Filtered Ports", open_filtered_ports)
print_ports("Closed|Filtered Ports", closed_filtered_ports)

flag=False
for port in open_ports:
    if common_ports[port][1]==1:
        print(Fore.RED + f"WARNING! Sensitive Port {port}: {common_ports[port][0]} is open via {open_ports[port][1]}" + Style.RESET_ALL)
        flag=True
if not flag:
    print("Congratulations! No sensitive ports open")        

file_option=input("Do you want to save results to a file?(Yes/No):")
if (file_option.lower()=="yes"):
    format_option=input("Enter File Format(txt/json):")
    if format_option.lower()=="txt":
        print("txt")
    elif format_option.lower()=="txt":
        print("json")