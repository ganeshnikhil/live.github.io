
import os  
import sys 

version = sys.version_info
if int(version[0])>=3 and int(version[1])>=5:
    print('....................................................................')
else:
    print('python  interpreture version is not satisfied ............ [download python 3]')
    print(exit())
    

try:   
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip install beautifulsoup4")
    from bs4 import BeautifulSoup


    
try:
    from prettytable import  PrettyTable  
except ImportError:
    os.system("pip install prettytable")
    from prettytable import  PrettyTable
    
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import  requests
    
try:
    import  lxml
except ImportError:
    os.system(" pip install lxml")
    
# install  all libraries ....... bs4 , requests,preettytable : os is built in module of python.
# to change the color
os.system('color 0a')

# request at the given to link to get data
response=requests.get('http://static.cricinfo.com/rss/livescores.xml')


# check the response code i. if 200 then it means website is responding 
print(response.status_code)


# use beautiful soup to scrap the website 
soup=BeautifulSoup(response.text,features='lxml')


# then we find all <description> tag from the response of website with the help of bs4 
result=soup.find_all('description')


# then print the date time of today 
print(os.system('Time/t')) 


# then find <pubdate> tag to get the details of data
date=soup.find('pubdate')


# then remove the tag by replace()
dat=str(date).replace('<pubdate>','')
print(dat.replace('</pubdate>',''))


# for numbering declare count variable to 0,,,
count=0


# create a preety table 
my_table= PrettyTable (['no.','match'])


# get the extract  details from description tag into my_table
for match in result:
    my_table.add_row([str(count),match.get_text()])
    # then increment........
    count=count+1
    
    
# the print my table 
print(my_table)

