# wiki-by-email

**wiki-by-email** is a simple Python application that lets you create and maintain a wiki through email. It was primarily conceived for personal knowledge management, but the possibilities are endless!

**Note:** This app is still under development. Watch this space (or the [project's repo](https://github.com/abithakt/wiki-by-email)) for updates!

<!---## Getting started

1. Clone or download the repo.

``` git clone ...
```

2. Rename `example-config.yml` to `config.yml`.
3. Enter your credentials. Make sure your mail server supports IMAP and X-GM-RAW. You may have to enable access for [less secure apps]() on Gmail.
4. Run `wiki-by-email.py`.
--->

## How it works

Most interaction with this app is by email; you make changes by emailing yourself or an email account whose credentials you provide to the app, which will monitor your inbox. The final wiki can be viewed in a browser.

* To create a page, send yourself an email with the page title and `[wiki][add]` in the subject line. The body or an attached markdown file serve as the page's contents. (`wiki` can be changed to a keyword of your preference in the config file.)
* To append text to a page, send yourself an email with the page title and `[wiki][append]` in the subject line. The body or an attached markdown file will be appended to the page.
* To edit a page, request the page from the server by emailing yourself `[wiki][request]` + the page title. The server will reply with the page contents, and you can reply with the edited content (in full).

More to come!

<!---
Installation)
Usage
Known issues
Contributing
License
--->

## Known issues

* Only Gmail and IMAP servers using X-GM-RAW are supported.
[](* Markdown attachments are not supported.)

[](## Thanks)

## Copyright and License

**wiki-by-email** is licensed under the Apache license. The full text of the license can be found [here](https://github.com/abithakt/wiki-by-email/blob/master/LICENSE).

**wiki-by-email** (c) 2018 Abitha K Thyagarajan

<!---
## Getting started
## to do
- [ ] add support for PGP
- [ ] add a search bar
- [ ] emoji favicons
--->
