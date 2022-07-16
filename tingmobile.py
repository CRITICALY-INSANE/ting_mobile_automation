#https://www.freelancer.com/projects/research/search-few-youtube-scripts
#https://www.freelancer.com/projects/python/need-perform-web-scraping-grab
#3.8.9

#refer_cross.png
#terms.png
#next.png
#simcard.txt
import re
import sys
import time
import threading
import pyperclip
import pyautogui
import traceback
import linecache
from time import sleep
from PIL import Image
from itertools import cycle
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.mouse import Button, Controller as mscon
from threading import Event, Thread

from pynput.keyboard import Key, Controller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.support import expected_conditions as EC

#send for SS.py


kb = Controller()
ms=mscon()
global i,mail,sim_card,imei,driver,var,strt_page,line_no
line_no=1
strt_page='https://tingmobile.com/mobile/activate/account'
i=0
near_time_pg=None
sim_card="8901240144704346979F"
#imei=


def helo():
    global driver,mail,var
    try:
        s1=(input("Please Enter From where You want to Start Mail ID \n -->   ting____@flingboxpro.com "))
        var=int(s1.strip())
        
        mail="ting"+str(var)+"@flingboxpro.com"
        print('Starting From ---->  '+ mail)
        
    except Exception as s:
        helo()
    

    initate()


def check_4_input(typo,element_id):
    global i
    global driver
    try:
        element_present = EC.presence_of_element_located((typo, str(element_id)))
        WebDriverWait(driver,1).until(element_present)
        i+=1                
    except Exception as e:
        check_4_input(typo,element_id)


def no_error(cur):
    global var
    time.sleep(10)
    while cur==driver.current_url:
        if not (check_exists_by_xpath('//*[@id="signupForm"]/p')):
             print('Error Detected')
             print('Using a new mail id')
             print('----->  ting'+str(var)+"@flingboxpro.com")
             var+=1
             
             driver.quit()
             initate()
        else:
            no_error(cur)
            time.sleep(10)
        
        
def photo(file_nme):
    time.sleep(2)
    try:
        pyautogui.click(file_nme)
    except Exception as e:
        photo(file_nme)


def check_exists_by_xpath(xpath):
    global driver
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True


def another_1():
    screenWidth, screenHeight = pyautogui.size()
    wd=screenWidth/3
    if (pyautogui.locateOnScreen('activate.PNG', region = (wd,0,wd,screenHeight)) is not None):
        return True
    else:
        return False

    
def final_showdown():
    global driver
    print('final_showdown')
    
    refer=('/html/body/div[3]/main/can-import/page-account-refer_a_friend/util-page-container/section/div/util-page-nav/nav/ul/li[4]/a/span[2]')
    check_4_input(By.XPATH,refer)
    driver_element(By.XPATH,refer).click()
    time_sleep(1)
    copy=('/html/body/div[3]/main/can-import/page-account-refer_a_friend/util-page-container/section/div/div/div[1]/referral-share/div/div[1]/div/div[1]/button')
    check_4_input(By.XPATH,copy)
    driver_element(By.XPATH,copy).click()
    time.sleep(0.5)
    clipboard_content = pyperclip.paste()
    f = open("for_demo.txt", "w+")
    
    f.write(clipboard_content)
    f.close()
    
    
def bck_to_accnt2():
    global driver
    print('bck_to_accnt2')

    new_phone_act='/html/body/div[3]/main/can-import/page-mobile-activate-welcome/section/div/section/div/a[1]'
    sign_in='/html/body/div[3]/main/can-import/page-mobile-activate-welcome/section/div/section/div/a[2]'
    check_4_input(By.XPATH,new_phone_act)
    check_4_input(By.XPATH,sign_in)
    w=another_1()
    if w== True:
        driver.find_element(By.XPATH,sign_in).click()
        final_showdown()
    else:
        driver.back()
        activate_device()
    
def bck_to_accnt():
    global driver
    tit=driver.current_url
    print('bck_to_accnt')
    present=('https://tingmobile.com/mobile/activate/process')
    if tit==present:
        time.sleep(3)
        bck_to_accnt()
    else:
        bck_to_accnt2()
    

def activate_device():
    global driver
    
    chk=('/html/body/div[3]/main/can-import/page-mobile-activate-confirm/section/div/div/form/div[1]/div/label/input')
    goo='/html/body/div[3]/main/can-import/page-mobile-activate-confirm/section/div/div/form/util-buttons/div/button'
    check_4_input(By.XPATH,goo)
    check_4_input(By.XPATH,chk)
    time.sleep(2)

    onechk=driver.find_element(By.XPATH ,chk).is_selected()
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    chk_boc='//*[@id="signupForm"]/div/fieldset[1]/fieldset/div/div/label[1]/input'
    check_4_input(By.XPATH,chk_boc)


    if onechk ==False:
        c1=driver.find_element(By.XPATH,chk)
        driver.execute_script("arguments[0].click();", c1)
    else:
        pass
    time.sleep(2)
    driver.find_element(By.XPATH,goo).click()
    print('activate_device')
    bck_to_accnt()
    
def activation():
    coords = pyautogui.locateOnScreen("done.png")
 
    # coords is None -> no result
    if coords is None:
        time.sleep(2)
        activation()
    else:
        return

def activation2():
    go_to=pyautogui.locateOnScreen('go to account.png')
    pyautogui.click(go_to)

def check_box(nme):
    try:
        go_to=pyautogui.locateOnScreen(nme)
        try:
            pyautogui.click(go_to)
        except Exception as espreso:
            print(traceback.format_exc())
            print(espreso)
            
    except Exception as espreso2:
        print(traceback.format_exc())
        print(espreso2)
     
def no_save():
    width, height= pyautogui.size()
    x=width
    y=height
    try:
        go_to=pyautogui.locateOnScreen('no_save.png',region=(int(width/3), 0 , int(width/3),height ))
        try:
            pyautogui.click(go_to)
        except Exception as espreso:
            print(traceback.format_exc())
            print(espreso)
            
    except Exception as espreso2:
        print(espreso2)
        print(traceback.format_exc())
    time.sleep(1)

def link():
    ck='/html/body/div[3]/main/can-import/page-mobile-activate-confirm/section/div/div/form/div[1]/div/label/input'
    driver.find_element(By.XPATH,ck).click()
    check_box('terms.png')
    
def pillow_thing():
    global quality1
    quality1=95
    #from PIL import Image
  
# Open the image by specifying the image path.
    image_path = "terms.png"
    image_file = Image.open(image_path)
    image_file.save("terms.png", quality=quality1)
    real_check_box('terms.png')
    
def real_check_box(img):
    global quality1
    bul=True
     #first SS file ..
    #then this file with terms.png
    width, height= pyautogui.size()
    x=width
    y=height
    
    try:
        go_to=pyautogui.locateOnScreen(img, region=(0,(height/3), (width/2),(height/3)))
        try:
            pyautogui.click(go_to)
        except Exception as espreso:
            bul=False
            print(traceback.format_exc())
            
    except Exception as espreso2:
        bul=False
        print(traceback.format_exc())

    if bul != True and quality1>0:
        pillow_thing()
    else:
        print('Actual quaity is '+quality1 )
        
def activate_device_photo():
    width, height= pyautogui.size()
    time.sleep(6)
    x=width
    y=int(height)
    no_save()
    y2=y/2
    y3=y2/2
    y4=int(y3/2+y2)
    ms.position=(x,y4)
    ms.press(Button.left)
    time.sleep(2)
    ms.release(Button.left)
    time.sleep(1)
    try:
        link()
    except Exception as Ef:
        print('line**********')
        print(traceback.format_exc())
        print(Ef)
    #photo('terms.png')
    #photo('next.png')
    real_check_box('terms.png')
    time.sleep(3)
    check_box('next.png')
    
    
    #activation()
    #activation2()

def account():
    global driver
    check_4_input(By.ID,'card_cvv')
    time.sleep(2)
    
    month = driver.find_element(By.XPATH,'//*[@id="card_expiry_month"]').click()
    time.sleep(1)
    kb.press('j')
    kb.release('j')
    time.sleep(1)
    kb.press('j')
    kb.release('j')
    time.sleep(0.5)
    kb.press(Key.enter)
    kb.release(Key.enter)
        
    year = driver.find_element(By.XPATH,'//*[@id="card_expiry_year"]').click()
    time.sleep(0.2)
    for i in range(2022,2027+1):
        kb.press(Key.down)
        kb.release(Key.down)
        time.sleep(0.5)
    kb.press(Key.enter)
    kb.release(Key.enter)
    
    #year.send_keys("2027")
    
    driver.find_element(By.ID,'cardholder_name').send_keys("Johen Barnett")
    time.sleep(1)
    driver.find_element(By.ID,'card_number').send_keys("4254185119840852")
    time.sleep(1)
    driver.find_element(By.ID,'card_cvv').send_keys("477")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    proceed=('//*[@id="billingForm"]/div/util-buttons/div/button')
    time.sleep(8)
    driver.find_element(By.XPATH,proceed).click()
    print('account')
    activate_device_photo()
    

def refereal(jk):
    x = threading.Timer(5,refereal, args=(1,)).start()    
    try:
        #print('Ghanta baja')
        driver.switch_to.default_content()
        driver.find_element(By.CLASS_NAME,'CloseButton__ButtonElement-sc-79mh24-0 eTnibx englewood-CloseButton englewood-close englewood-ClosePosition--top-right').click()

    except Exception as ff:
        pass

    
def refe():
    global kk
    i=0
    width, height= pyautogui.size()
    height2=height/2
    #time.sleep(1)
    try:
        go_to=pyautogui.locateOnScreen('refer_cross.png',region=(int(width/2), int((height/2)-100) , int(width/2), int(height/2)+100))
        #print(go_to)
        try:
            pyautogui.click('refer_cross.png')
            print('Found Pop UP')
        except Exception as Espr:
            pass
            
    except Exception as e:
        print(e)
        print('absent')
        print(traceback.format_exc())
            

    
        
def voucher():
    global driver,kk
    kk=1
    print('voucher')
    time.sleep(2)
    
    #refe()
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    bt=('//*[@id="content"]/can-import/page-mobile-order-plans/section/div/util-plans/div[2]/div[2]/util-plans-plancard/div/button')
    check_4_input(By.XPATH,bt)
    driver.find_element(By.XPATH,bt).click()
    para='//*[@id="content"]/can-import/page-mobile-order-number/section/div/div/section/form/util-select-block[2]/div'
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    check_4_input(By.XPATH,para)
    driver.find_element(By.XPATH,para).click()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.ID,"areaCode")
    time.sleep(2)
    
    nx='//*[@id="content"]/can-import/page-mobile-order-number/section/div/div/section/form/util-buttons/div/button'
    check_4_input(By.XPATH,nx)
    driver.find_element(By.XPATH,nx).click()
    account()
##    try:
##        account()
##    except Exception as pr:
##        er = open("error_file.txt", "w+")
##        er.write(str(pr))
##        line=(traceback.format_exc())
##        er.write(str('-----------------------------------'))
##        er.write(str(line))
##        er.close()
##        

def agey():
    global line_no,sim_card
    time.sleep(1)
    check_4_input(By.ID,'iccid')
    time.sleep(3)
    conti=('//*[@id="iccidForm"]/util-buttons/div/button')

    driver.find_element(By.ID,'iccid').send_keys(sim_card)
    time.sleep(1)
    try:
        conti=('//*[@id="iccidForm"]/util-buttons/div/button')
        driver.find_element(By.XPATH,conti).click()
    except Exception as ass:
        pass
    time.sleep(2)
    
    try:
        partxt='//*[@id="iccidForm"]/fieldset/field-group/div/p'
        txt=driver.find_element(By.XPATH,partxt)
        html = txt.get_attribute('innerHTML')
        
        if 'Sorry, this SIM card cannot be activated.' == html.strip():
            er = open("simcard.txt", "r")
            
            sim_card=(er.readline(20))          
              
            with open("simcard.txt", 'r') as fp:
                for count, line in enumerate(fp):
                    pass
            print('Total Lines', str(count + 1))
            fp.close()
            total_lines=int(count + 1)
            
            with open("simcard.txt") as f2:
                data = (f2.read()).strip()
            f2.close()
            with open("simcard.txt",'w') as again:
                again.write(data)
            again.close()
            with open("simcard.txt",'r') as again2:
                data = (again2.read()).strip()
                first=data.split('\n', 20)[0]
                sec=data.split('\n', 20)[1]
                last=data.split('\n')[-1]
                #last=data.split('\n', 20)[total_lines-2]
                
                        
            again2.close()
            print(' ')
            print('New Simcard-------->  '+first)
            with open("simcard.txt",'w') as cut:
                new_data=(data.replace(first,'    '))
                new_data2=new_data.strip()
                cut.write(new_data2)
            cut.close()
                
            
            driver.refresh()
            line_no+=1
            agey()
        else:
            #print('sab sahi')
            return
    except Exception as papu:
        print(papu)
        return
        
def sim_page():
    global driver,sim_card
    
    sim_option='//*[@id="content"]/can-import/page-mobile-byod-device/section/div/div[2]/a'
    check_4_input(By.XPATH,sim_option)
    driver.find_element(By.XPATH,sim_option).click()
    agey()

    #check for new page
    check_4_input(By.ID,'address_streetAddress')
    driver.find_element(By.ID,'address_streetAddress').send_keys("104 Hillside CT")
    driver.find_element(By.ID,'address_addressLine2').send_keys(" ")
    driver.find_element(By.ID,'address_cityName').send_keys("Stafford")
    time.sleep(2)
    driver.find_element(By.ID,'address_stateCode').click()
    time.sleep(2)
    kb.press('v')
    kb.release('v')
    time.sleep(1)
    kb.press(Key.down)
    kb.release(Key.down)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)
    driver.find_element(By.ID,'address_postalCode').send_keys("22554")
    nxt=('//*[@id="content"]/can-import/page-mobile-order-service/section/div/div/section/form/util-buttons/div/button')
    driver.find_element(By.XPATH,nxt).click()
    print('sim_page')

    voucher()

    

def captha():
    global driver
    try:
        element_present = EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]'))
        element_present =EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border")).click()
        WebDriverWait(driver,1).until(element_present)
    except Exception as ass:
        captha()
    
def enabled():
        WebDriverWait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
        return

def for_being_human(pathx):
    gg=pathx
    element = driver.find_element(By.XPATH,pathx)
    prop = element.get_property('disabled')
    time.sleep(2)
    if prop==True:
        for_being_human(gg)
    else:
        return
    
def imei():
    #refer to documentation
    global vele,ele
    global driver
    
    pro='//*[@id="content"]/can-import/page-mobile-byod-device/section/div/div/section/form/util-buttons/div/button'
    check_4_input(By.XPATH,pro)
    
    driver.find_element(By.ID,'deviceSerialNumber').send_keys("353160102696502")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)    
    
    
    #new_sim=('//*[@id="content"]/can-import/page-mobile-byod-device/section/div/div[2]/a')
    
    check=('//*[@id="content"]/can-import/page-mobile-byod-device/section/div/div/section/form/util-buttons/div/button')
    check_4_input(By.XPATH,check)
    element = driver.find_element(By.XPATH,check)
    prop = element.get_property('disabled')
    if prop==True:
        enabled()
    print (prop)
    time.sleep(1)  
    driver.switch_to.default_content()
    for_being_human(check)
    driver.find_element(By.XPATH ,check).click()
    print('imei')
    #driver.find_element(By.XPATH ,check).click()


    sim_page()
    

def nxt_page():
    global driver,pp12
    driver.maximize_window()
    
    pp12="//p[text()='If you have a phone already in hand, start here.']"
    gose='//*[@id="content"]/can-import/page-mobile-byod-landing/section/div/div/section/form/util-buttons/div/button'
    check_4_input(By.XPATH,pp12)
    check_4_input(By.XPATH,gose)
    driver.find_element(By.XPATH,pp12).click()
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.XPATH,gose).click()
    #imei page
    print('nxt_page')
    imei()
    

def some_set():
    global driver
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    time.sleep(2)
    driver.get('chrome://flags')
    driver.find_element(By.ID,'search').send_keys("WebGL")
    op='//*[@id="enable-webgl-developer-extensions"]/div/div[2]/select'
    bp='//*[@id="enable-webgl-draft-extensions"]/div/div[2]/select'
    check_4_input(By.XPATH,op)
    driver.find_element(By.XPATH,op).click()
    kb.press(Key.down)
    kb.release(Key.down)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)
    driver.find_element(By.XPATH,bp).click()
    time.sleep(1)
    kb.press(Key.down)
    kb.release(Key.down)
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)
    check_4_input(By.ID,"experiment-restart-button")
    driver.find_element(By.ID,"experiment-restart-button").click()
    time.sleep(4)
    
def strt_thread(interval, func):
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func()
    Thread(target=loop).start()    
    return stopped.set

    
def initate():
    global driver,mail,var,pp12,strt_page
    options = Options()

    strt_thread(3,refe)
    print('initate')
    
    #options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #driver = webdriver.Firefox(executable_path='C:/Users/super/AppData/Local/Programs/Python/Python36/tingMobile/geckodriver.exe', options=options)

##    options = webdriver.ChromeOptions()
##    options.add_experimental_option("useAutomationExtension", False)
##    options.add_experimental_option("excludeSwitches",["enable-logging"])
##    options.add_argument("--start-maximized")
##    options.add_argument("--enable-webgl")
##    options.add_argument("--enable-webgl-developer-extensions")
##    options.add_argument("--enable-webgl-draft-extensions")
##    path=('C:/Users/super/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
##    driver = webdriver.Chrome(executable_path=path,options=options)
    
    part=GeckoDriverManager().install()
    options = Options()
    
    options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'    
    path=Service(part)
    #path=('C:/Users/super/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
    driver = webdriver.Firefox(service=path,options=options)
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    


    #driver = webdriver.Chrome(executable_path=path,options=options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    #some_set()cd 
    global mail
    driver.get(strt_page)
    check_4_input(By.ID,'full_name')
    
    
##    if (len(driver.window_handles)>1):
##        
##        window_name = driver.window_handles[0]
##        
##        driver.switch_to.window(window_name=window_name)
##        #driver.close()
##        
##        
##                
##        #driver.get(strt_page)
##        #check_4_input(By.ID,'full_name')
##        
##        
    try:
        if(str(add)!='[]'):
            #print(add[0])
            bha=str(add[0])
            check_4_input(By.ID,'full_name')
            #return str(add[0])
        
        

    except Exception as e:
        bha=''
        
    i=0
    
    driver.maximize_window()
    time.sleep(2)
    #some_set()
    #refereal(1)

    
    
    driver.find_element(By.ID,'full_name').send_keys("Bill Klein")
    driver.find_element(By.ID,'email').send_keys(mail)
    driver.find_element(By.ID,'phone').send_keys("7036778538")
    k=driver.find_element(By.XPATH,'//*[@id="signupForm"]/div/fieldset[1]/fieldset/div/div/label[1]/input').is_selected()
    k2=driver.find_element(By.XPATH,'//*[@id="signupForm"]/div/fieldset[1]/fieldset/div/div/label[2]/input').is_selected()
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    if k==True:
        c1=driver.find_element(By.XPATH,'//*[@id="signupForm"]/div/fieldset[1]/fieldset/div/div/label[1]/input')
        driver.execute_script("arguments[0].click();", c1)
    else:
        pass
    if k2==True:
        c2=driver.find_element(By.XPATH,'//*[@id="signupForm"]/div/fieldset[1]/fieldset/div/div/label[2]/input')
        driver.execute_script("arguments[0].click();", c2)
    sb=driver.find_element(By.XPATH,'//*[@id="signupForm"]/div/fieldset[1]/div[6]/button')
    time.sleep(2)
    sb.click()
    #time.sleep(4)
    #no_error(near_time_pg)
    
  
    check_4_input(By.XPATH,"//p[text()='If you have a phone already in hand, start here.']")
    nxt_page()

try:
    
    helo()
except Exception as exc:
    print('Try Again')
    print(exc)
