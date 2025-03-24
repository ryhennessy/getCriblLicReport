#!/usr/bin/python3

import sys
import requests
import getpass
import datetime
import urllib3
    
#Added to remove any warning messages from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

loginData = {}
criblHeaders = {"Content-type": "application/json", "Accept": "application/json"}

# Uncomment and set the following values for the URL, login, and password
# to hard-code them. The script will then not prompt for the values via stdin
############################################################################
# criblUrl = "http://cribleader.com"
# loginData['username'] = 'admin'
# loginData['password'] = "Mypassword1"
#############################################################################

if "criblUrl" not in vars() or loginData == {}:
    criblUrl = input("Cribl Leader URL (https://leader.examle.com): ").rstrip()
    loginData["username"] = input("Login: ").rstrip()
    loginData["password"] = getpass.getpass("Password: ")

criblAuthUrl = criblUrl + ":9000/api/v1/auth/login"
criblLicUrl = criblUrl + ":9000/api/v1/system/licenses/usage"

try:
    resp = requests.post(criblAuthUrl, json=loginData, headers=criblHeaders,verify=False)
    criblToken = resp.json()["token"]
except Exception:
    print("\nLogin Failed")
    print("------------------------------------")
    print(str(resp.status_code) + " " + resp.text)
    sys.exit(1)


criblHeaders["Authorization"] = "Bearer " + criblToken

resp = requests.get(criblLicUrl, headers=criblHeaders,verify=False)
licData = resp.json()

outputCSV = criblUrl.split("://")[1] + "-usage.csv"

with open(outputCSV, "w") as csvfile:
    csvfile.write("Date, Gigabytes In, Gigabytes Out, Events In, Events Out")
    line = "\n"
    for i in range(licData["count"]):
        line += datetime.datetime.fromtimestamp(
            (licData["items"][i]["startTime"] / 1000) + 21600
        ).strftime("%m-%d-%y")
        line += f",{str(float(licData['items'][i]['inBytes'])/1000000000)}"
        line += f",{str(float(licData['items'][i]['outBytes'])/1000000000)}"
        line += f",{licData['items'][i]['inEvents']}"
        line += f",{licData['items'][i]['outEvents']}"
        csvfile.write(line)
        line = "\n"

print(f"\nDone! Data saved to {outputCSV}")
