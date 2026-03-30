'''
Take a filename "data.txt" and check for mail-adresses
return those adresses in a tidy fashion, so they can be copied and used with
email-program.
'''

# get regular expression-functionality
import re

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

