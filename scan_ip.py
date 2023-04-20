import os
import socket
import pandas as pd
import time
from datetime import datetime

# Create an empty DataFrame to store the results
lista_ips = pd.read_excel("lista_ips.xlsx") if os.path.isfile("lista_ips.xlsx") else pd.DataFrame(columns=['IP', 'Hostname'])
conflitos_ips = pd.read_excel("conflitos_ips.xlsx") if os.path.isfile("conflitos_ips.xlsx") else pd.DataFrame(columns=['Data', 'IP', 'Host original', 'Host novo'])

def check_hostname(ip_address, hostname):
    global conflitos_ips, lista_ips
    if hostname is None:
        print("Sem nome, continuando")
        return
    if ip_address in lista_ips['IP'].values:
        df_filtered = lista_ips[lista_ips['IP'] == ip_address]
        if df_filtered['Hostname'].values[0] == hostname:
            print("Mesmo IP e mesmo nome, seguindo em frente")
        else:
            print("Conflito de IP detectado")
            former_hostname = df_filtered['Hostname'].values[0]
            lista_ips.loc[lista_ips['IP'] == ip_address, 'Hostname'] = hostname
            new_hostname = hostname
            change_dict = {'Data': datetime.now(), 'Host original': former_hostname, 'Host novo': new_hostname, 'IP': ip_address}
            conflitos_ips = pd.concat([conflitos_ips, pd.DataFrame([change_dict])])
            print(change_dict)
    else:
        print("Não existe")
        lista_ips = pd.concat([lista_ips, pd.DataFrame([{'IP': ip_address, 'Hostname': hostname}])])

# Define the IP address ranges to scan
ip_ranges = ['172.17.16.', '172.17.17.']

# Define the number of hosts to scan for each range
num_hosts = 255

# Define the interval between pings in seconds
ping_interval = 300

num_pings = 1
timeout = 1200

# Define the ping command to use
ping_command = f'ping -n {num_pings} -w {timeout} '
ping_command += '{}'

# Loop over each IP range and each host in the range, and ping it
while True:
    for ip_range in ip_ranges:
        for i in range(1, num_hosts + 1):
            ip_address = ip_range + str(i)
            print(f"Pingando {ip_address}...")
            response = os.system(ping_command.format(ip_address))        
            if response == 0:
                try:
                    hostname = socket.gethostbyaddr(ip_address)[0]
                except:
                    hostname = None
                check_hostname(ip_address, hostname)
    
    # Wait for the specified interval before pinging again
    while True:
        try:
            lista_ips.to_excel("lista_ips.xlsx", index=False)
            conflitos_ips.to_excel("conflitos_ips.xlsx", index=False)
            break
        except Exception:
            input(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: Não foi possível escrever as planilhas. Provavelmente o arquivo está aberto, por favor feche e aperte Enter...")
    
    print(f"Aguardando {ping_interval} segundos.")
    time.sleep(ping_interval)