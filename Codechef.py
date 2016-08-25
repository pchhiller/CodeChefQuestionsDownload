from bs4 import BeautifulSoup
import urllib2
import mechanize

response = urllib2.urlopen('https://www.codechef.com/problems/school')
data =response.read()
start="https://www.codechef.com"
soup = BeautifulSoup(data)
for link in soup.find_all('tr', class_="problemrow"):
    Name=link.b.string
    end=link.a.get('href')
    Url= start+end
    SuccesfulSolutions= link.find('div',style="text-align:center;").string
    print Url
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
            print data1
        i=i+1
    break




