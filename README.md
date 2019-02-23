# PyRecover [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/)
A Python and PHP based system to recover and log passwords from Chrome.

# Requirements
- Python 3.x.
- A webserver with PHP installed.
- Various Python dependancies (you can see them in the main script.)
- PyInstaller

# Current Status
Currently, a very crude backend and the recovery script have been finished. Currently the known issues is the data file not deleting after it uploads itself to the webserver.

# How to use this program
- Clone the repo and upload the files in the "Site" folder to your website.
- Run the python script and build a recovery file.
- Run the recovery file on the computer you desire to recover the passwords of and check your website.

# Future plans
- GUI for the builder
- Better backend with a login system
- Support for multiple uploads (right now it only lets you have one data file.)

# Disclaimer
This program is made for educational and personal use only. It is not to be used to steal others passwords and I'm not responsible for any consequences should you get caught doing so.
