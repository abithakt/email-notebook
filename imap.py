# https://stackoverflow.com/questions/31703739/how-to-read-email-using-python-3

import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('login@gmail.com', 'password')
