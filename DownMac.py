import os
import requests
import subprocess
print("DownMac 1.0.0")

url = "https://apple.com" # checking github account

try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"{url} is reachable.")
    else:
        print(f"{url} returned status code {response.status_code}")
except requests.RequestException as exept:
    print(f"Failed to reach {url}. Error: {exept}")


    
print("\n\n1.  macOS 26")
print("2.  macOS 15")
print("3.  macOS 14")
print("5.  macOS 13")
print("6.  macOS 12")
print("7.  macOS 11")
print("8.  macOS 10.12")
print("9.  Mac OS X 10.11")
print("10. Mac OS X 10.10")
print("11. Mac OS X 10.8")
print("12. Mac OS X 10.7")
choice = input("Select a version to download: ")
subprocess.run(['python', 'download.py', choice])