import requests
import socket
print(""" 
                       _                 
                      (_)                
 _   _ _ __ __ _ _ __  _ _   _ _ __ ___  
| | | | '__/ _` | '_ \| | | | | '_ ` _ \ 
| |_| | | | (_| | | | | | |_| | | | | | |
 \__,_|_|  \__,_|_| |_|_|\__,_|_| |_| |_|
                                         
                                         
""")
# URL do alvo
url = "http://www.example.com/"

# Envia a solicitação
r = requests.get(url)

# Verifica se o site está online
if r.status_code == 200:
    print("Site está online!")

    # Verifica a proteção do site
    if r.headers['X-XSS-Protection'] == '1; mode=block':
        print("Site protegido contra XSS!")
    else:
        print("Site não protegido contra XSS!")

    # Verifica os domínios escondidos
    print("Domínios escondidos:")
    for link in r.text.split(' '):
        if link.startswith('http'):
            print(link)

    # Verifica os IPs logados
    print("IPs logados:")
    for ip in socket.gethostbyname_ex(url)[2]:
        print(ip)

else:
    print("Site está offline!")