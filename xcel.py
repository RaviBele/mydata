from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import requests
import shutil
from PIL import Image
import pytesseract



def save_image_to_file(image, dirname, suffix):
    with open('{dirname}/img_{suffix}.jpg'.format(dirname=dirname, suffix=suffix), 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)


usernameStr = 'SFC250820185758'
passwordStr = 'rpb@gslab123'

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get(('http://www.xcelnetwork.in/Default.aspx'))
username = browser.find_element_by_id('txt_Uname')
username.send_keys(usernameStr)
password = browser.find_element_by_id('txt_pass')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_id('Button4')
nextButton.click()
for i in range(28550354, 28550405):
    select_forn_no= Select(browser.find_element_by_id('ContentPlaceHolder1_drp_pagejump'))
    select_forn_no.select_by_value(str(i))
    image = browser.find_element_by_tag_name("img")
    img_src = image.get_attribute("src")
    save_img = requests.get(img_src, stream=True)
    save_image_to_file(save_img, ".", 1)
    img = Image.open('img_1.jpg')
    data = pytesseract.image_to_string(img)
    print pytesseract.image_to_string(Image.open('./img_1.jpg'), lang='eng')
    formdata = data.split("\n")
    while '' in formdata:
        formdata.remove('')
    formdata1 = formdata[0].split(" ")
    formdata2 = formdata[1].split(" ")
    formdata3 = formdata[2].split(" ")
    formdata4 = formdata[3].split(" ")
    formdata5 = formdata[4].split(" ")
    formdata6 = formdata[5].split(" ")
    formdata7 = formdata[6].split(" ")

    ip = formdata1[0]
    first = formdata1[1]
    last = formdata1[2]
    ipAddress = browser.find_element_by_id('ContentPlaceHolder1_txt_ipaddress')
    ipAddress.send_keys(ip)
    firstname = browser.find_element_by_id('ContentPlaceHolder1_txt_firstname')
    firstname.send_keys(first)
    lastname = browser.find_element_by_id('ContentPlaceHolder1_txt_lastname')
    lastname.send_keys(last)


    addr = formdata2[0]
    for j in range(1, len(formdata2) - 2):
        addr += " "+formdata2[j]
    city = formdata2[len(formdata2)-2]
    state = formdata2[len(formdata2)-1]
    address = browser.find_element_by_id('ContentPlaceHolder1_txt_address')
    address.send_keys(addr)
    cityname = browser.find_element_by_id('ContentPlaceHolder1_txt_city')
    cityname.send_keys(city)
    statecode = browser.find_element_by_id('ContentPlaceHolder1_txt_state')
    statecode.send_keys(state)

    zipCode = formdata3[0]
    Home = formdata3[1]
    Phone = formdata3[2]
    zip = browser.find_element_by_id('ContentPlaceHolder1_txt_zipcode')
    zip.send_keys(zipCode)
    homePhone = browser.find_element_by_id('ContentPlaceHolder1_txt_homephone')
    homePhone.send_keys(Home)
    workPhone = browser.find_element_by_id('ContentPlaceHolder1_txt_workphone')
    workPhone.send_keys(Phone)

    email = formdata4[0]
    dob = formdata4[len(formdata4)-2]
    ssn = formdata4[len(formdata4)-1]
    mailid = browser.find_element_by_id('ContentPlaceHolder1_txt_email')
    mailid.send_keys(email)
    dobirth = browser.find_element_by_id('ContentPlaceHolder1_txt_dob')
    dobirth.send_keys(dob)
    ssnID = browser.find_element_by_id('ContentPlaceHolder1_txt_ssn')
    ssnID.send_keys(ssn)

    dlnumber = formdata5[0]
    dlstate = formdata5[1]
    bankaba = formdata5[2]
    dlNo = browser.find_element_by_id('ContentPlaceHolder1_txt_dlnumber')
    dlNo.send_keys(dlnumber)
    dlSt = browser.find_element_by_id('ContentPlaceHolder1_txt_dlstate')
    dlSt.send_keys(dlstate)
    bankABA = browser.find_element_by_id('ContentPlaceHolder1_txt_bankaba')
    bankABA.send_keys(bankaba)

    accno = formdata6[0]
    accNo = browser.find_element_by_id('ContentPlaceHolder1_txt_bankacnumber')
    accNo.send_keys(accno)
    bankName = browser.find_element_by_id('ContentPlaceHolder1_txt_bankname')
    bankName.send_keys("Bank Of Am")
    employer=""
    try:
        k = formdata6.index("Am")
        employer=formdata6[k+1]
        for l in range(k+2, len(formdata6)):
            employer += " "+formdata6[l]
    except ValueError:
        employer=formdata6[len(formdata6)-1]
    employerCompany = browser.find_element_by_id('ContentPlaceHolder1_txt_employer')
    employerCompany.send_keys(employer)

    dohire = formdata7[0]
    supervisor = formdata7[1]
    supervisorNo = formdata7[2]
    doHire = browser.find_element_by_id('ContentPlaceHolder1_txt_datehired')
    doHire.send_keys(dohire)
    superVisor = browser.find_element_by_id('ContentPlaceHolder1_txt_supername')
    superVisor.send_keys(supervisor)
    supervisorNumber = browser.find_element_by_id('ContentPlaceHolder1_txt_superphone')
    supervisorNumber.send_keys(supervisorNo)

    saveButton = browser.find_element_by_id('ContentPlaceHolder1_btn_submit')
    saveButton.click()



