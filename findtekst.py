#!/usr/bin/env python3

'''
Take a filename as input, convert the file to .txt and check for mail-adresses
inside it. return those adresses in a tidy fashion, so they can be copied
 and used with email-program.
'''

import os
import re
import pypandoc

# get user input on which file to make
originalFile = input("indtast filnavn her: ")

# convert the filetype to plaintext
output = pypandoc.convert_file(originalFile, 'plain', outputfile=".data.txt")

try:
    file = open(".data.txt")

    # identify emails in the .txt file.
    for line in file:
        line = line.strip()
        emails = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+.[0-9a-zA-z]+", line)
             
        if(len(emails) > 0):
            
            maillist = []
            
            # add each mail to empty list
            for mail in emails:

                # check if mail is already in list
                if mail not in maillist:
                    maillist.append(mail)

            # write a new file with a column of the emails
            with open("extracted_emails.txt", "a") as f:
                for mail in maillist:
                    f.write(f"{mail}\n")

except FileNotFoundError as e:
    print(e)
    
