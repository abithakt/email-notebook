import logging
import smtplib
import ruamel.yaml as yaml

# Open config file
with open("config.yml", 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

mailserver = smtplib.SMTP(config['gmail']['smtp_server'], config['gmail']['smtp_port'])
mailserver.ehlo()
mailserver.starttls()
mailserver.login(config['email'], config['password'])
