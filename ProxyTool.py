#By: https://github.com/Amir-78

import argparse;
import requests;
import sys;
import urllib.request , socket
from colorama import Fore;
from colorama import Style;


#Main Function

def main():
    print(Fore.GREEN + " ___                              _____                _   \n(  _`\                           (_   _)              (_ ) \n| |_) ) _ __    _          _   _   | |     _      _    | | \n| ,__/'( '__) /'_`\ (`\/')( ) ( )  | |   /'_`\  /'_`\  | | \n| |    | |   ( (_) ) >  < | (_) |  | |  ( (_) )( (_) ) | | \n(_)    (_)   `\___/'(_/\_)`\__, |  (_)  `\___/'`\___/'(___)\n                          ( )_| |                          \n                          `\___/'                          [By: github.com/Amir-78]\n\n\n")
    cmdsParser = argparse.ArgumentParser(description='ProxyTool created get proxies fast and check them.')
    cmdsParser.add_argument("--google", help="Get google proxies.", dest='google', action='store_true', default=False)
    cmdsParser.add_argument("--https", help="Get https proxies.", dest='https', action='store_true', default=False)
    cmdsParser.add_argument("--count", help="The proxies count (Default: 10)", dest='count', default=10, type=int)
    cmdsParser.add_argument("--timeout", help="Connection Timeout (Default: 15)", dest='timeout', default=15, type=int)
    cmds = cmdsParser.parse_args()
    print(Style.RESET_ALL)
    getP(cmds.google, cmds.https, cmds.count, cmds.timeout)

#Get Function

def getP(google, https, count, timeout):

    print(Fore.RED + f'\n+ ProxyTool Started with options:\n\n- Google: {google}\n- Https: {https}\n- Count: {count}\n- Timeout: {timeout}\n\n')
    print(Style.RESET_ALL)
    API1 = 'http://pubproxy.com/api/proxy?limit=5'

    rapi1 = requests.get(url=API1)
    if rapi1.status_code == 200:
        for proxy in rapi1.json()["data"]:
            isGoogle = False
            isHttps = False

            if proxy["support"]["google"] == 1:

                isGoogle = True

            if proxy["support"]["https"] == 1:

                isHttps = True
            Filter(proxy["ip"], proxy["port"], proxy["type"], proxy["country"], isGoogle, isHttps, google, https, count, timeout)

    API2 = 'https://gimmeproxy.com/api/getProxy?post=true&get=true&maxCheckPeriod=3600&anonymityLevel=1'

    rapi2 = requests.get(url=API2)
    if rapi2.status_code == 200:

        proxy2 = rapi2.json()
        isGoogle = False
        isHttps = False

        if proxy2["websites"]["google"]:

            isGoogle = True

        if proxy2["supportsHttps"]:

            isHttps = True

        Filter(proxy2["ip"], proxy2["port"], proxy2["type"], proxy2["country"], isGoogle, isHttps, google, https, count, timeout)
    API3 = 'https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&filterLastChecked=10'
    rapi3 = requests.get(url=API3)
    if rapi3.status_code == 200:
        for proxy3 in rapi3.json()["data"]:
            isGoogle = False
            isHttps = True

            if proxy3["google"]:

                isGoogle = True
            Filter(proxy3["ip"], proxy3["port"], proxy3["protocols"][0], proxy3["country"], isGoogle, isHttps, google, https, count, timeout)




#Filter Function

def Filter(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout):

    if google:
        if isGoogle:
            if https:
                if isHttps:
                    Check(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout)
                    return
            else:
                Check(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout)
                return
    else:
        if https:
            if isHttps:
                Check(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout)
                return
        else: 
            Check(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout)
            return


#Check Function
countNow = 0
def Check(ip, port, type, country, isGoogle, isHttps, google, https, count, timeout):
    socket.setdefaulttimeout(timeout)
    protocol = "http"
    if isHttps:
        protocol = "https"
    try:        
        proxyH = urllib.request.ProxyHandler({f'{protocol}': f'{ip}:{port}'})        
        OPR = urllib.request.build_opener(proxyH)
        OPR.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.24 Safari/537.36')]
        urllib.request.install_opener(OPR)        
        sock=urllib.request.urlopen('http://api.ipify.org/')
    except urllib.error.HTTPError as e:        
        return True
    except Exception as detail:
        return True
    global countNow
    if countNow >= count:
        return sys.exit()
    countNow += 1
    return Printer(ip, port, type, country, isGoogle, isHttps)

def Printer(ip, port, type, country, isGoogle, isHttps):
    print(Fore.CYAN + f'{type} {ip} {port}\n#Country: {country} Google: {isGoogle} Https: {isHttps}')
    print(Style.RESET_ALL)
    return

#Call Main Function

main()

#By: https://github.com/Amir-78
