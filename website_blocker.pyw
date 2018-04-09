#ToDo add comments to code
#look into editing other files based on time

import time
from datetime import datetime as dt

hosts_temp=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path=r"D:\goldf\Documents\Coding and College\Python Projects\megaCoursePY\web_block\hosts"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,22) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23,50):
        print("working hours....")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours....")
    time.sleep(5)
