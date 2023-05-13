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
print(R+" Merhaba! Ben Python kullanıyorum.  TG: dark_enza"+R)
print("")
print(Y+" İnternetsiz SSL/SNI Test Aracı"+Y)
print(R+" Telegram Kanalım : @dwstoree"+R)


while True:
    secimyap = input(M+'[1] Hostu elle gir\n[2] Hostu host.txt dosyasından al\n[3] Cikis\nSeçiminiz: '+M)

    if secimyap == '1':
        hostlar = input('Hostu gir (Çoklu ise boşluk ile ayırın): ').split()
        break
    elif secimyap == '2':
        with open('host.txt', 'r') as f:
            hostlar = f.read().splitlines()
        break
    elif secimyap == '3':
        exit()
    else:
        print(R+'Yanlış seçim yaptınız. Tekrar deneyin.'+R)
        time.sleep(2)

with open('baglananlar.txt', 'w') as baglananlar:
    pass

with open('baglananlar.txt', 'a') as baglananlar:
    for host in hostlar:
        sonuc = subprocess.run(['timeout', '2', 'openssl', 's_client', '-connect', 'ssl.dark-enza.club:443', '-servername', host], capture_output=True, text=True)

        if 'CONNECTED' in sonuc.stdout:
            print(Y+f'{host}: BAĞLANTI BAŞARILI'+Y)
            baglananlar.write(f'{host}\n')
        else:
            print(R+f'{host}: BAĞLANTI BAŞARISIZ'+R)
