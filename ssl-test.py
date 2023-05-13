import subprocess
import time

M = "\033[34m"
Y = "\033[32m"
R = "\033[31m"

print(M+"  _____             _      ______                "+M)
print(M+" |  __ \           | |    |  ____|               "+M)
print(M+" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ "+M)
print(M+" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |"+M)
print(M+" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |"+M)
print(M+" |_____/ \__,_|_|  |_|\_\ |______|_| |_/_/ \__,_|"+M)
print(R+" ‎Merhaba! Ben Python kullanıyorum.  TG: dark_enza"+R)
print("")
print(Y+" Internetsiz SSL/SNI Test Araci"+Y)
print(R+" Telegram Kanalim : @dwstoree"+R)


while True:
    secimyap = input(M+'[1] Hostu elle gir\n[2] Hostu host.txt dosyasindan al\n[3] Cikis\nSeciminiz: '+M)

    if secimyap == '1':
        hostlar = input('Hostu gir (Coklu ise bosluk ile ayirin): ').split()
        break
    elif secimyap == '2':
        with open('host.txt', 'r') as f:
            hostlar = f.read().splitlines()
        break
    elif secimyap == '3':
        exit()
    else:
        print(R+'Yanlis secim yaptiniz. Tekrar deneyin.'+R)
        time.sleep(2)

with open('baglananlar.txt', 'w') as baglananlar:
    pass

with open('baglananlar.txt', 'a') as baglananlar:
    for host in hostlar:
        sonuc = subprocess.run(['openssl', 's_client', '-connect', 'ssl.dark-enza.club:443', '-servername', host], capture_output=True, text=True, timeout=2)

        print(sonuc)
        if 'CONNECTED' in sonuc.stdout:
            print(Y+f'{host}: BAGLANTI BASARILI'+Y)
            baglananlar.write(f'{host}\n')
        else:
            print(R+f'{host}: BAGLANTI BASARISIZ'+R)
