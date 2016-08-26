# -*- coding: UTF-8 -*-
import pdfkit
from bs4 import BeautifulSoup
import urllib2
import mechanize
import os
list1=[]
list2=[]
difficulty= 'school'
if not os.path.exists(difficulty):
    os.makedirs(difficulty)
for file in os.listdir("./"+difficulty+"/"):
    list1.append(file)
for item in list1:
    index = item.index(' ')
    list2.append(item[index+1:-4])
def partmatch(name):
    for i in range(0,len(list2)):
        if list2[i]==name:
            return i
    return 0




options = {
    'quiet': '',
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

response = urllib2.urlopen('https://www.codechef.com/problems/'+difficulty)

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
        os.rename("./"+difficulty+"/"+list1[ind],PdfName)
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
            os.rename(PdfName, "./"+difficulty+"/"+PdfName)

        i=i+1




