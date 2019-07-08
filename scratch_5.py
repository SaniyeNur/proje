import socket
import subprocess
from datetime import datetime
import time
import sys


class renkler:
   PEMBE = '\033[95m'
   MAVİ = '\033[94m'
   YESİL = '\033[92m'
   SARI = '\033[93m'
   KIRMIZI = '\033[91m'


print(renkler.YESİL + '''

                 [ PENETRASYON TESTERS ]
                  [ PORT TARAMA ARACI ]
    ''')
print("")
print(renkler.KIRMIZI + "[!] Logdef Siber Güvenlik Departmanı Port Tarama Aracıdır.")
print("")
hedefip = input(renkler.MAVİ + "[?] Hedef Sistem İP si Giriniz : ")
print("")
print("Hedef Taranıyor... ", hedefip)
try:
   for port in range(1, 1025):
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       result = sock.connect_ex((hedefip, port))
       if result == 0:
           print("Port {}:      Açık".format(port))
       sock.close()

except KeyboardInterrupt:
   print("Çıkış Yaptınız")
   sys.exit()

except socket.gaierror:
   print("Hedef İP Tanımlı Değil")
   sys.exit()

except socket.error:
   print("Sunucuya Bağlanılamadı")
   sys.exit()
print(renkler.KIRMIZI + "Coded by Saniye Nur Çintimur - LOGDEF ")

start = time.time()
"the code you want to test stays here"
end = time.time()
print(end - start)