import email, logging, mistletoe
import ruamel.yaml as yaml
from imapclient import IMAPClient as imapc
from datetime import datetime



# Open config file

with open("config.yml", 'r') as ymlfile:
	config = yaml.safe_load(ymlfile)



#if "gmail.com"
#last accessed...

last_accessed = datetime.now()


# Log in

mail = imapc(config['gmail']['imap_server'], use_uid = True, ssl = True)
rv = mail.login(config['email'], config['password'])



# List mailboxes

mailboxes = mail.list_folders()
mailboxes = [str(x) for x in mailboxes]



# Find the name of the 'All Mail' folder

all = str("")
for a in mailboxes:
    if "\All" in a:
        all = a[a.index('['):a.index(')', -2)]

all = all[:-1]



# Open 'All Mail'

allmail = mail.select_folder(all)



# Identify messages from self/custom 'from' address

from_messages = mail.search(['FROM', config['from']])

# from_messages = mail.search(['FROM', config['from'], 'SINCE', config['last_accessed'], 'SUBJECT', config['flags']['wiki']])

print(from_messages)

#----------------------------------------------------------------------------------



# Identify messages with '[wiki]'/custom flag

wikipage = []
for msgid, data in mail.fetch(from_messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    #print(envelope.from_)
    if str(config['flags']['wiki']) in str(envelope.subject): wikipage.append(msgid)
    #print("ID \#%d: '%s' received %s" % (msgid, envelope.subject, envelope.date))

print(wikipage)


# Get email body

#messages = mail.search(['NOT DELETED'])
response = mail.fetch(from_messages, ['RFC822', 'BODY[TEXT]'])
print(data)
for msgid, data in response.items():
        parsedEmail = email.message_from_string(from_messages)
        body = email.message_from_string(data['BODY[TEXT]'])
        parsedBody = parsedEmail.get_payload(0)
        print(parsedBody)


# Close folder and log out

mail.close_folder()
mail.logout()
