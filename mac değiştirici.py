import subprocess
import optparse

yeni = optparse.OptionParser()

yeni.add_option("-i", "--interface", dest="interface", help="Arayüz değiştirme:")
yeni.add_option("-m", "-mac", dest="mac_address", help="Yeni MAC adresi")

(yeni, mac) = yeni.parse_args()
arayuz = yeni.interface
mac_adresi = yeni.mac_address

subprocess.call(["ifconfig", arayuz, "down"])
subprocess.call(["ifconfig", arayuz, "hw", "ether", mac_adresi])
subprocess.call(["ifconfig", arayuz, "up"])

print("MAC adresi değiştirildi.")
