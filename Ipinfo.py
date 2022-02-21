from textwrap import indent
import requests
import json

info = open("response.json","w")
with open("sample.txt","r") as read_ioc:
    file = []
    for i in read_ioc: 
        file.append(i.rstrip())
  

    for j in file:

        search=requests.get("https://ipinfo.io/"+j+"?token=936ebbcd3be427")
        print(search.json())
        data = search.json()
       
        write_response = json.dump(data, info)
        info.write("\n")
            


        





