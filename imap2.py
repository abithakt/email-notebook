import email, logging, mistletoe
import ruamel.yaml as yaml
from imapclient import IMAPClient as imapc
from datetime import datetime



# Open config file
with open('config.yml', 'r+') as ymlfile:
    config = yaml.safe_load(ymlfile)
    

    
# Record time of last access - TODO
last_accessed = datetime.now()



# Log in
mail = imapc(config['gmail']['imap_server'], use_uid = True)
rv = mail.login(config['email'], config['password'])



# List mailboxes
mailboxes = mail.list_folders()
mailboxes = [str(x) for x in mailboxes]



# Find the name of the 'All Mail' folder in Gmail
all = str("")
for a in mailboxes:
    if "\All" in a:
        all = a[a.index('['):a.index(')', -2)]
all = all[:-1]



# Open 'All Mail'
allmail = mail.select.folder(all)



# Identify messages from self or from custom address
from_messages = mail.search(['FROM', config['from']])



# Identify messages with '[wiki]' or custom flag

# Close folder and log out
mail.close_folder()
mail.logout()
