# -*- coding: UTF-8 -*-
import pdfkit
from bs4 import BeautifulSoup
import urllib2
import mechanize
import os
list1=[]
for file in os.listdir("./"):
    list1.append(file)
def partmatch(name):

    for i in range(0,len(list1)):
        if(name in list1[i]):
            return i
    return 0




options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

response = urllib2.urlopen('https://www.codechef.com/problems/school')
data =response.read()
start="https://www.codechef.com"
soup = BeautifulSoup(data)
for link in soup.find_all('tr', class_="problemrow"):
    Name=link.b.string
    end=link.a.get('href')
    Url= start+end
    SuccesfulSolutions= link.find('div',style="text-align:center;").string
    PdfName=SuccesfulSolutions+" "+Name+'.pdf'
    print Name
    if (PdfName in list1):
        print "Skipping" +PdfName+" , because file already exists"
        continue
    elif (partmatch(Name)!=0):
        ind=partmatch(Name)
        os.rename(list1[ind],PdfName)
        print "Renaming..."
        continue


    br = mechanize.Browser()
    br.set_handle_robots(False)
    response=br.open(Url)
    i=1
    data= response.read()
    soup=BeautifulSoup(data)
    html=""
    for data1 in soup.find_all('div',class_="content"):
        if i==2:
            #for child in data1.descendants:
                #html=html +child.encode('utf-8')
            #print data1
            print "Converting to pdf " + PdfName
            data1= str(data1)
            html=data1.decode('utf-8')
            pdfkit.from_string(html,PdfName,options=options)
        i=i+1




