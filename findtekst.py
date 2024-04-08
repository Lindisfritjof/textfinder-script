from bs4 import BeautifulSoup
import re
from pathlib import Path

# directory
with open("Digitale-Licenser-Hjemmeside-main/index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# find all the anchor tags with "href"  
# attribute starting with "https://" 
with open('links.txt', 'w') as f:
    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    # display the actual urls
     print(link.get('href'), file=f)


