#!/usr/bin/python3

import requests
import getpass 
import datetime

loginData={}

#Uncomment and set the following values for the url, login, and password 
# to hard codd them. The script will then not probmpt for the values via stdin
############################################################################
# criblUrl = "http://criblurl.local"
# loginData['username'] = 'admin'
# loginData['password'] = "Mypassword1"
#############################################################################

criblHeaders={'Content-type': 'application/json', 'Accept': 'application/json'}


if 'criblUrl' not in vars() or loginData == {}:
    criblUrl = input("Cribl Leaader URL (https://leader.examle.com): ").rstrip()
    loginData['username'] = input("Login: ").rstrip()
    loginData['password'] = getpass.getpass("Password: ")

criblAuthUrl = criblUrl + ":9000/api/v1/auth/login"
criblLicUrl = criblUrl + ":9000/api/v1/system/licenses/usage"

try:
    resp = requests.post(criblAuthUrl, json=loginData, headers=criblHeaders)
    criblToken = resp.json()['token']

except Exception:
    print("\nLogin Failed")
    print("------------------------------------")
    print(str(resp.status_code) + " " + resp.text)
    exit(1)

criblHeaders['Authorization'] = "Bearer " + criblToken

resp=requests.get(criblLicUrl, headers=criblHeaders)
licData=resp.json()


with open('usage.csv', 'w') as csvfile:
    csvfile.write('Date, Gygabytes In, Bytes Out, Events In, Events Out')
    line="\n"
    for i in range(licData['count']):
       line+=datetime.datetime.fromtimestamp((1734307200000/1000)+21600).strftime('%m-%d-%y %H')
       line+=f",{str(int(licData['items'][i]['inBytes'])/1000000000)}"                                                                           
       line+=f",{str(int(licData['items'][i]['outBytes'])/1000000000)}"                                                                           
       line+=f",{licData['items'][i]['inEvents']}"                                                                           
       line+=f",{licData['items'][i]['outEvents']}"      
       csvfile.write(line)
       line="\n"


