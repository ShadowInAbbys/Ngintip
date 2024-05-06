import sys
import socket

def get_ip(target_host):
    try:
        ip = socket.gethostbyname(target_host)
        return ip
    except socket.gaierror:
        print("sory ip-nya ga ada bro, coba cek ulang domainnya atau jaringan lu ya")
        sys.exit()

def ngintip():
    print("   _______    ___     ___________     ____                       ")
    print("  |   |   |  |   |   |    ___   |    |    |         ()()()       ")
    print("  |   ||   | |   |   |   |   |  |    |____|        ()    ()      ")
    print("  |   | |   ||   |   |   |   |__|     ____        ()******()     ")
    print("  |   |  |   |   |   |   |  _____    |    |      ()&&&@@&&&()    ")
    print("  |   |   |  |   |   |   | |__  |    |    |      ()&&&@@&&&()    ")
    print("  |   |    |     |   |   |   |  |    |    |       ()******()     ")
    print("  |   |     |    |   |   |___|  |    |    |        ()    ()      ")
    print("  |___|      |___|   |__________|    |____|         ()()()  ngintip v1.0")
    print("")
    print("Ngintip => Information gathering tools")
    print("")

def subdomainscanner(target_host):
    print("\n[+] Subdomain Scanner Start!")
    wordlist = ["mail", "localhost", "blog", "forum", "0", "01", "02", "03", "1", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2", "20", "3", "3com", "4", "5", "6", "7", "8", "9", "ILMI", "a", "a.auth-ns", "a01", "a02", "a1", "a2", "abc", "about", "ac", "academico", "acceso", "access", "accounting", "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin", "administracion", "administrador", "administrator", "administrators", "admins", "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates", "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai", "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind", "am", "amarillo", "americas", "an", "anaheim", "analyzer", "announce", "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app", "app01", "app1", "apple", "application", "applications", "apps", "appserver", "aq", "ar", "archie", "arcsight", "argentina", "arizona", "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena", "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto", "av", "aw", "ayuda", "az", "b", "b.auth-ns", "b01", "b02", "b1", "b2", "b2b", "b2c", "ba", "back", "backend", "backup", "baker", "bakersfield", "balance", "balancer", "baltimore", "banking", "bayarea", "bb", "bbdd", "bbs", "bd", "bdc", "be", "bea", "beta", "bf", "bg", "bh", "bi", "billing", "biz", "biztalk", "bj", "black", "blackberry", "blogs", "blue", "bm", "bn", "bnc", "bo", "bob", "bof", "boise", "bolsa", "border", "boston", "boulder", "boy", "br", "bravo", "brazil", "britian", "broadcast", "broker", "bronze", "brown", "bs", "bsd", "bsd0", "bsd01", "bsd02", "bsd1", "bsd2", "bt", "bug", "buggalo", "bugs", "bugzilla","cpanel"]

    print("[+] Total wordlist size: " + str(len(wordlist)))

    for sublist in wordlist:
        sub_host = sublist + "." + target_host
        try:
            ip = get_ip(sub_host)
            print("[+] " + sub_host + " ===> " + ip)
        except Exception:
            pass

    print("\n[+] Subdomain Scanner Complete!")

if __name__ == "__main__":
    ngintip()
    target_host = input("\nEnter hostname/domain/sub-domain: ")

    print("\n[+] Select an Option\n")
    print("1. Get IP Address")
    print("2. Subdomain Scanner")

    option = int(input("[+] Select Option\n    > "))
    if option == 1:
        IP = get_ip(target_host)
        print("\n{} IP Address is ==> {}".format(target_host, IP))
    elif option == 2:
        subdomainscanner(target_host)
    else:
        print("[+] Incorrect Option selected")