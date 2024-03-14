import pyautogui as pag
import pandas as pd
import time
import socket 
import logging

def check_internet():
    '''
    credits: https://gist.github.com/ghsatpute/7df3256fcd7114116473b5ddb0a0c54f
    '''
        
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname('www.google.com')
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        logging.info('Internet connectivity is present')
        return True
    except Exception as e:
        logging.error('Internet connectivity is not present: {}'.format(e))
        return False

def waitUntilThereIsSomeConnectionWithInternet():
    time_limit_until_my_patience_ends = 60
    while True:
        time.sleep(1)
        time_limit_until_my_patience_ends -= 1
        if time_limit_until_my_patience_ends == 0:
            exit()
        if check_internet():
            break
        else:
            continue

# sets as 0.5 secs the pause time between each command of PyAutoGUI
pag.PAUSE = 0.5

# enters at the system's website for this class
pag.press('win')
pag.write('brave')
pag.press('enter')
pag.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pag.press('enter')

# checks the connection with internet
waitUntilThereIsSomeConnectionWithInternet()

# waits the website to load
time.sleep(5)

# sets the email and password used for the login
EMAIL = 'LucasLongo.intensivaoPython.aula1@gmail.com'
PASSWORD = '1234'

# it logins. It's just that.
pag.press('tab')
pag.write(EMAIL)
pag.press('tab')
pag.write(PASSWORD)
pag.press('tab')
pag.press('enter')

 # checks the connection with internet
waitUntilThereIsSomeConnectionWithInternet()

# waits the website to load
time.sleep(5)
 
# reads the sheet at produtos.csv file
sheet = pd.read_csv('001/produtos.csv')

for row in sheet.index:
    pag.click(x=410, y=254) # clicks on the first field
    pag.write(str(sheet.loc[row,'codigo']))
    pag.press('tab')
    pag.write(str(sheet.loc[row,'marca']))
    pag.press('tab')
    pag.write(str(sheet.loc[row,'tipo']))
    pag.press('tab')
    pag.write(str(sheet.loc[row,'categoria']))
    pag.press('tab')
    pag.write(str(sheet.loc[row,'preco_unitario']))
    pag.press('tab')
    pag.write(str(sheet.loc[row,'custo']))
    pag.press('tab')
    if not pd.isna(sheet.loc[row,'obs']):
        pag.write(str(sheet.loc[row,'obs']))
    pag.press('tab')
    pag.press('enter')
    pag.press('home')

print("T-T-That's all folks! Thanks for testing this program!")
exit()