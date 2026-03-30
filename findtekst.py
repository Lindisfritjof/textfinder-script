'''
Take a filename as input, convert the file to .txt and check for mail-adresses
inside it. return those adresses in a tidy fashion, so they can be copied
 and used with email-program.
'''

import re
import fileinput
import pypandoc

originalFile = input("indtast filnavn her: ")
output = pypandoc.convert_file(originalFile, 'plain', outputfile="data.txt")

try:
    file = open("data.txt")  # open the file
    for line in file:
        line = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+.[0-9a-zA-z]+", line)
        if(len(emails) > 0):

            # print a nice, clean column of emails
            for mail in emails:
                print(mail)

except FileNotFoundError as e:
    print(e)
