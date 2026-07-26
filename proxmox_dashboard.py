import requests
import os 
from dotenv import load_dotenv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

auth_url = "https://192.168.1.4:8006/api2/json/access/ticket"
payload = {
    "password": os.environ["PROXMOX_PASSWORD"],
    "username": os.environ["PROXMOX_USERNAME"],
    "realm": os.environ["PROXMOX_REALM"]
}

auth_response = requests.post(auth_url, json=payload, verify=False)
ticket = auth_response.json()["data"]["ticket"]

stats_url = "https://192.168.1.4:8006/api2/json/cluster/resources"
cookies = {"PVEAuthCookie": ticket}

stats_response = requests.get(stats_url, cookies=cookies, verify=False)

resources = stats_response.json()["data"]

print("=== Homelab Status ===")
for item in resources:
    if item["type"] =="lxc":
        print(item["name"], item["status"])



