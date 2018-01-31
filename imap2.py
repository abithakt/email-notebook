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
