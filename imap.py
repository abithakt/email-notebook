import imaplib
import ruamel.yaml as yaml

with open("config.yml", 'r') as ymlfile:
	config = yaml.safe_load(ymlfile)

#print(config['gmail']['imap_server'])

mail = imaplib.IMAP4_SSL(config['gmail']['imap_server'])
mail.login(config['email'], config['password'])
