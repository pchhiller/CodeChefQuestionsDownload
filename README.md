# CodeChefQuestionsDownload
Downloads questions from codechef as separate pdf files.
Requires:
```
pdfkit :pip install pdfkit
pdfkit needs wkhtmltopdf to work .[Instructions] (https://pypi.python.org/pypi/pdfkit)
```
Replace 'school' in line 30 with 'easy', 'medium','hard' and 'challenge' for changing difficulty 
>response = urllib2.urlopen('https://www.codechef.com/problems/school')

Run again if some error occurs. It wont replace pre-existing files and only download the ones that haven't been downloaded yet.
