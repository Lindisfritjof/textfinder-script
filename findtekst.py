'''
Take a filename as input, convert the file to .txt and check for mail-adresses
inside it. return those adresses in a tidy fashion, so they can be copied
 and used with email-program.
'''

import re
import fileinput
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

            # write extracted emails to new file
            with open("extracted_emails.txt", "a") as f:
                for mail in emails:
                    f.write(f"{mail}\n")

except FileNotFoundError as e:
    print(e)
