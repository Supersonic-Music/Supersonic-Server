import subprocess
import time
import sys

def check_phone_connected():
    connected = input("Is your phone connected? [Y/n]: ")
    if connected.upper() == "N":
        print("Please connect your phone via USB...")
        return False
    else:
        return True

def get_phone_ip():
    result = subprocess.run(["adb", "shell", "ip -4 -o addr show wlan0 | awk '{print $4}'"], stdout=subprocess.PIPE, text=True)
    output = result.stdout.strip()
    return output

def get_phone_hostname():
    hostname = subprocess.run("adb shell getprop ro.product.model", stdout=subprocess.PIPE, text=True, shell=True)
    output = hostname.stdout.strip()
    return output

def connect():
    while not check_phone_connected():
        print("Plug in your phone and make sure ADB is enabled...")
    
    hostname = get_phone_hostname()
    print(f"Your {hostname} is connected!")
    ip_address = get_phone_ip()[:-3]
    print(f"Phone's IP address: {ip_address}")
    return ip_address

def connect_wifi(ip_address):
    subprocess.run("adb tcpip 5555", shell=True)
    wireless_command = f"adb connect {ip_address}"
    print(wireless_command)
    time.sleep(2)
    subprocess.run(wireless_command, shell=True)
    subprocess.run("scrcpy -e -w -t --window-title='GrayJay - Sonic Screwdriver'", shell=True)

if __name__ == "__main__":
    ip_address = connect()
    connect_wifi_yes_no = input("Would you like to switch to wireless mode? [Y/n]: ")
    if connect_wifi_yes_no == "N":
        subprocess.run("scrcpy -d -w -t --window-title='GrayJay - Sonic Screwdriver'", shell=True)
    else:
        connect_wifi(ip_address)
