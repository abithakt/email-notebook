import pyzmail, logging, mistletoe, imaplib
import ruamel.yaml as yaml
from imapclient import IMAPClient as imapc
from datetime import datetime


imaplib._MAXLINE = 10000000


# Open config file

with open("config.yml", 'r') as ymlfile:
	config = yaml.safe_load(ymlfile)



#if "gmail.com"
#last accessed...

last_accessed = datetime.now()


# Log in

mail = imapc(config['gmail']['imap_server'], use_uid = True, ssl = True)
rv = mail.login(config['email'], config['password'])



# List mailboxes -- TODO: move this to setup file

mailboxes = mail.list_folders()
mailboxes = [str(x) for x in mailboxes]



# Find the name of the 'All Mail' folder -- TODO: move this to setup file, write to config

all = str("")
for a in mailboxes:
    if "\All" in a:
        all = a[a.index('['):a.index(')', -2)]
all = all[:-1]



# Open 'All Mail'

allmail = mail.select_folder(all)



# Identify messages from self/custom 'from' address -- only works for Gmail

search_string = 'from:' + str(config['from']) + ' "' + str(config['flags']['wiki']) + '"'

#from_messages = mail.search(['FROM', config['from']]) #?
from_messages = mail.gmail_search(search_string)

print(from_messages)

#----------------------------------------------------------------------------------



# Get email bodies
wikipages = mail.fetch(from_messages, ['BODY[]', 'FLAGS']).items()
print(wikipages)
"""for k in wikipages: # iterate through dict
    message = pyzmail.PyzMessage.factory(k['BODY[]']) #??
    print(message.text_part.get_payload().decode(message.text_part.charset))"""

# Close folder and log out

mail.close_folder()
mail.logout()
