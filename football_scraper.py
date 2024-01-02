from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import re
import csv
import os
url= 'https://www.fantacalcio-online.com/it/serie-a/2021-2022/voti'
utr2="https://www.goal.com/it/notizie/fantacalcio-formazioni-titolari-serie-a-2022-2023/blt704877d1959a81f6"
path="C:\\Users\\lucat\\OneDrive\\Desktop\\experimento"
driver=webdriver.Chrome()
driver.get(utr2)
time.sleep(2)
html=driver.page_source
doc1=BeautifulSoup(html,"html.parser")
doc1=doc1.find(class_="article-body_body__JAkqy body")
squads=doc1.find_all(["p"])
sep=":"
players=[]
temp=[]
for i in range(43):
    if(i>3 and i%2==0):

        temp=re.split(r"[:\;\,\.]",squads[i].text)
        temp.pop(0)
        temp.pop(-1)
        players=players+temp


for i in range(len(players)):
    players[i] = players[i].lower()
    players[i]=players[i][1:]


driver.get(url) 
time.sleep(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"iubenda-cs-banner\"]/div/div/div/div[3]/div[2]/button[2]"))).click()
role=WebDriverWait(driver,20).until(
                EC.element_to_be_clickable((By.XPATH,"//*[@id=\"players_list\"]/thead/tr[2]/th[1]")))

role.click()
time.sleep(4)
nameP=[]
squadraP=[]
fantaMediaP=[]
partitegiocateP=[]
quotazioneP=[]
giocabileP=[]

nameD=[]
squadraD=[]
fantaMediaD=[]
partitegiocateD=[]
quotazioneD=[]
giocabileD=[]

nameC=[]
squadraC=[]
fantaMediaC=[]
partitegiocateC=[]
quotazioneC=[]
giocabileC=[]

nameA=[]
squadraA=[]
fantaMediaA=[]
partitegiocateA=[]
quotazioneA=[]
giocabileA=[]

for k in range(46):
    html=driver.page_source
    doc= BeautifulSoup(html,"html.parser")
    a=doc.find_all(["tbody"])
    b=a[1]
    c=b.find_all(["tr"])
    for j in c:
        d=j.find_all(["td"])
        if((d[0].text.split()[0]=="P") and(d[4].text.split()[0]!="0") and( d[6].text!='')):
            nameP.append(d[2].text.split()[0])
            squadraP.append(d[1].text)
            partitegiocateP.append(float(d[4].text.split()[0]))
            quotazioneP.append(float(d[3].text.split()[0]))
            if(d[2].text.split()[0].split()[0].lower() in players):
                giocabileP.append(1)
            else:
                giocabileP.append(0)

            try:
                q=round((float(d[6].text)*float(d[4].text.split()[0]))//(float(d[3].text)+1),2)
                fantaMediaP.append(float(d[6].text))

            except:
                fantaMediaP.append(float("0"))

        if((d[0].text.split()[0]=="D")  and(d[4].text.split()[0]!="0") and( d[6].text!='')):
            nameD.append(d[2].text)
            squadraD.append(d[1].text)
            partitegiocateD.append(float(d[4].text.split()[0]))
            quotazioneD.append(float(d[3].text.split()[0]))
            if(d[2].text.split()[0].split()[0].lower() in players):
                giocabileD.append(1)
            else:
                giocabileD.append(0)

            try:
                q=round((float(d[6].text)*float(d[4].text.split()[0]))//(float(d[3].text)+1),2)
                fantaMediaD.append(float(d[6].text))

            except:
                fantaMediaD.append(float("0"))

        if((d[0].text.split()[0]=="C") and(d[4].text.split()[0]!="0" ) and( d[6].text!='')):
            nameC.append(d[2].text)
            squadraC.append(d[1].text)
            partitegiocateC.append(float(d[4].text.split()[0]))
            quotazioneC.append(float(d[3].text.split()[0]))
            if(d[2].text.split()[0].split()[0].lower() in players):
                giocabileC.append(1)
            else:
                giocabileC.append(0)

            try:
                q=round((float(d[6].text)*float(d[4].text.split()[0]))//(float(d[3].text)+1),2)
                fantaMediaC.append(float(d[6].text))

            except:
                fantaMediaC.append(float("0"))

        if((d[0].text.split()[0]=="A")  and(d[4].text.split()[0]!="0") and( d[6].text!='')):
            nameA.append(d[2].text)
            squadraA.append(d[1].text)
            partitegiocateA.append(float(d[4].text.split()[0]))
            quotazioneA.append(float(d[3].text.split()[0]))
            if(d[2].text.split()[0].split()[0].lower() in players):
                giocabileA.append(1)
            else:
                giocabileA.append(0)

            try:
                q=round((float(d[6].text)*float(d[4].text.split()[0]))//(float(d[3].text)+1),2)
                fantaMediaA.append(float(d[6].text))

            except:
                fantaMediaA.append(float("0"))

    time.sleep(3)

    pages=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"players_list_next"))
    )
    pages.click()

    time.sleep(2)


os.chdir(path)
newfolder="astaprova"
os.makedirs(newfolder)
os.chdir(path+"\\"+newfolder)

with open("astastatsP","a",newline="") as f:
        fieldnames=["name","giocabile","fantaM","quotazione","partitegioc","squadra"]
        thewriter =csv.DictWriter(f,fieldnames=fieldnames)

        thewriter.writeheader()

        for i in range(len(nameP)):
            thewriter.writerow({"name": nameP[i],"giocabile": giocabileP[i], "fantaM": fantaMediaP[i], "quotazione":quotazioneP[i],"partitegioc":partitegiocateP[i],"squadra":squadraP[i]}) 
with open("astastatsD","a",newline="") as f:
        fieldnames=["name","giocabile","fantaM","quotazione","partitegioc","squadra"]
        thewriter =csv.DictWriter(f,fieldnames=fieldnames)

        thewriter.writeheader()

        for i in range(len(nameD)):
            thewriter.writerow({"name": nameD[i],"giocabile": giocabileD[i], "fantaM": fantaMediaD[i], "quotazione":quotazioneD[i],"partitegioc":partitegiocateD[i],"squadra":squadraD[i]}) 
with open("astastatsC","a",newline="") as f:
        fieldnames=["name","giocabile","fantaM","quotazione","partitegioc","squadra"]
        thewriter =csv.DictWriter(f,fieldnames=fieldnames)

        thewriter.writeheader()

        for i in range(len(nameC)):
            thewriter.writerow({"name": nameC[i],"giocabile": giocabileC[i], "fantaM": fantaMediaC[i], "quotazione":quotazioneC[i],"partitegioc":partitegiocateC[i],"squadra":squadraC[i]}) 
with open("astastatsA","a",newline="") as f:
        fieldnames=["name","giocabile","fantaM","quotazione","partitegioc","squadra"]
        thewriter =csv.DictWriter(f,fieldnames=fieldnames)

        thewriter.writeheader()

        for i in range(len(nameA)):
            thewriter.writerow({"name": nameA[i],"giocabile": giocabileA[i], "fantaM": fantaMediaA[i], "quotazione":quotazioneA[i],"partitegioc":partitegiocateA[i],"squadra":squadraA[i]}) 





