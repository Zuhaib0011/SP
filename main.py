import requests, string, random, argparse, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate():
    nick = getRandomText(8)
    passw = getRandomString(12)
    email = nick+"@"+getRandomText(5)+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.16 Android/22 (SM-N976N)",
             "Spotify-App-Version": "8.6.16",
             "App-Platform": "Android",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, nick+":"+r.json()["username"]+":"+email+":"+passw)
        else:
            #Details in r.json()["errors"]
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1", type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
    parser.add_argument("-o", "--output", help="output file, default prints to the console")
    args = parser.parse_args()

    N = args.number if args.number else 1
    file = open(args.output, "w") if args.output else sys.stdout

    print("Generating accounts in the following format:", file=sys.stdout)
    print("NICKNAME:USERNAME:EMAIL:PASSWORD\n", file=sys.stdout)
    for i in range(N):
        result = generate()
        if result[0]:
            print(result[1], file=file)
        else:
            print(str(i+1)+"/"+str(N)+": "+result[1], file=sys.stdout)

    if file is not sys.stdout: file.close()
#------------LOGIN--------------

usr=input('Enter Email Id:') 
pwd=input('Enter Password:') 
driver = webdriver.Firefox(executable_path=r"C:\Users\sarsa\Downloads\geckodriver.exe")
driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')
sleep(1)
  
username_box = driver.find_element_by_id('login-username')
username_box.send_keys(usr)
sleep(1)
  
password_box = driver.find_element_by_id('login-password')
password_box.send_keys(pwd)
 
login_box = driver.find_element_by_id('login-button')
login_box.click()
sleep(2)

search = (136,262)
pyautogui.click(search)
sleep(2)
bar = (472,142)
pyautogui.click(bar)
sleep(2)
pyautogui.write('Zuhaib Fayaz')
