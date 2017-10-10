# -*- coding: UTF-8 -*-
import pdfkit  # used for creating pdf
from bs4 import BeautifulSoup  # the scrape data from Code Chef
import urllib2  # to get and post requestd using url
import mechanize  # your backend browser
import os  # for arranging into folders and renaming files
list1 = []  # Creating an empty list
list2 = []
difficulty = 'school'  # enter your prefered level in place of school

# making the folder for specified difficulty
if not os.path.exists(difficulty):
    os.makedirs(difficulty)
for file in os.listdir("./" + difficulty + "/"):  # For loop
    list1.append(file)
for item in list1:
    index = item.index(' ')
    list2.append(item[index + 1:-4])


def partmatch(name):
    for i in range(0, len(list2)):
        if list2[i] == name:
            return i
    return 0


# adjust your page display settings here
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
Editorial = "http://discuss.codechef.com/problems/"
response = urllib2.urlopen('https://www.codechef.com/problems/' + difficulty)

data = response.read()
start = "https://www.codechef.com"
j = 0
soup = BeautifulSoup(data)

# Gets question code
for link in soup.find_all('tr', class_="problemrow"):
    j = j + 1
    Name = link.b.string
    Code = Name[9:]
    print Code
    end = link.a.get('href')
    Url = start + end
    SuccesfulSolutions = link.find('div', style="text-align:center;").string
    # level by no. of solutions
    PdfName = SuccesfulSolutions + " " + Name + '.pdf'
    print Name
    if (PdfName in list1):
        print "Skipping" + PdfName + " , because file already exists"
        continue
    elif (partmatch(Name) != 0):
        ind = partmatch(Name)
        os.rename("./" +
                  difficulty +
                  "/" + list1[ind], "./" + difficulty + "/" + PdfName)
        print "Renaming..."
        continue

# opening and saving questions.
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open(Url)
    i = 1
    data = response.read()
    soup = BeautifulSoup(data)
    html = ""
    for data1 in soup.find_all('div', class_="content"):
        if i == 2:
            print "Converting to pdf " + PdfName
            data1 = str(data1)
            html = data1.decode('utf-8')
            pdfkit.from_string(html, PdfName, options=options)
            os.rename(PdfName, "./" + difficulty + "/" + PdfName)

        i += 1

print j
