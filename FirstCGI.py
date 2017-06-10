from urllib import urlopen
import re


webpage = urlopen('https://news.ycombinator.com/').read

patstring = re.compile('<a href=".*" class="storylink">(.*)</a>')

findpattitle = re.findall(patstring, webpage)


listfirstten = []
listfirstten[:] = range(1, 10)


for i in listfirstten:
    print findpattitle[i]