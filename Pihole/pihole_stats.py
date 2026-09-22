import requests
import os
from dotenv import load_dotenv

load_dotenv()

auth_url = "http://192.168.1.18/api/auth"
payload = {
    "password": os.environ["PIHOLE_PASSWORD"]
}

auth_response = requests.post(auth_url, json=payload)
sid = auth_response.json()["session"]["sid"]

status_url = "http://192.168.1.18/api/stats/summary"
custom_headers = {
    "X-FTL-SID": sid
}

stats_response = requests.get(status_url, headers=custom_headers)

total_queries = stats_response.json()["queries"]["total"]
blocked_queries = stats_response.json()["queries"]["blocked"]
percent_blocked = stats_response.json()["queries"]["percent_blocked"]
cached = stats_response.json()["queries"]["cached"]

print("=== Total Queries ===")
print(total_queries)
print("=== Blocked Queries ===")
print(blocked_queries)
print("=== Percent Blocked ===")
print(percent_blocked)
print("=== Cache ===")
print(cached)