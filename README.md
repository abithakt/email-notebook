**wiki-by-email** is a simple Python application that lets you create and maintain a wiki through email. This is primarily meant for personal knowledge management.

**Note:** This app is still under development and is in no shape to be viewed by the public at the time of writing (Jan 29, 2018). Watch this space (or the [project's repo](https://github.com/abithakt/wiki-by-email)) for updates!

## How it works

Most interaction with this app is by email; you make changes by emailing yourself or an email account whose credentials you provide to the app, which will monitor your inbox. The final wiki can be viewed in a browser.

* To create a page, send yourself an email with the page title and `[wiki][add]` in the subject line. The body or an attached markdown file serve as the page's contents. (`wiki` can be changed to a keyword of your preference in the config file.)
* To append text to a page, send yourself an email with the page title and `[wiki][append]` in the subject line. The body or an attached markdown file will be appended to the page.
* To edit a page, request the page from the server by emailing yourself `[wiki][request]` + the page title. The server will reply with the page contents, and you can reply with the edited content (in full).

More to come!
