from bs4 import BeautifulSoup
import re
from pathlib import Path

# Open the directory as a file to be parsed
with open("Digitale-Licenser-Hjemmeside-main/index.html") as fp:

# Parse the file.
    soup = BeautifulSoup(fp, 'html.parser')

# find and write all the anchor tags with "href" attribute also starting with "https://"
with open('links.txt', 'w') as f:
    # display the actual urls one at the time
    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        print(link.get('href'), file=f)


