import imaplib, email
import ruamel.yaml as yaml

# Open config file
with open("config.yml", 'r') as ymlfile:
	config = yaml.safe_load(ymlfile)

#if "gmail.com"

# Log in
mail = imaplib.IMAP4_SSL(config['gmail']['imap_server'])
mail.login(config['email'], config['password'])
#mail.select('inbox')

# List mailboxes
rv, mailboxes = mail.list()

# Find the name of the 'All Mail' folder
all = str("")
for i in mailboxes:
    if "\All" in str(i, 'utf-8'):
        a = str(i, 'utf-8')
        all = a[a.index('['):a.index('"', -1)]
all = '"' + all
all = all + '"'

# Open 'All Mail'
rv, data = mail.select(all)

#------------------------------------------------------------------------------

# Fetch all emails in 'All Mail'
rv, data = mail.search(None, "ALL")
print(data[0])

a = """for i in str(data[0], 'utf-8').split(): # data[0].split() gets email IDs
    rv, data = mail.fetch(i, '(RFC822)')
    msg = email.message_from_string(data[0][1])
    print( 'Message %s: %s' % (num, msg['Subject']))
    print('Raw Date:', msg['Date'])
    date_tuple = email.utils.parsedate_tz(msg['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(
            email.utils.mktime_tz(date_tuple))
        print( "Local Date:", \
            local_date.strftime("%a, %d %b %Y %H:%M:%S"))
"""

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))

b = """ .
def fetch_message(conn, msg_uid ):

    rv, data = conn.uid('fetch', msg_uid, "(RFC822)")
    if rv != 'OK':
        print "ERROR fetching message #", msg_uid
        return {}

    return email.message_from_string(data[0][1])  # dict-like object
"""
c = """ 
def get_recipients(msg_parsed):
    recipients = []
    addr_fields = ['From', 'To', 'Cc', 'Bcc']

    for f in addr_fields:
        rfield = msg_parsed.get(f, "") # Empty string if field not present
        rlist = re.findall(ADDR_PATTERN, rfield)
        recipients.extend(rlist)

return recipients
"""

# Store most recent email's timestamp in config file

# log out
mail.close()
mail.logout()
