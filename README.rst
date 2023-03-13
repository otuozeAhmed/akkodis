Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You will need to have the following installed:

- make - https://www.gnu.org/software/make/
- Docker - https://www.docker.com/products/docker-desktop/
- No third party library used - The Docker build will automatically install Python.

This project requires **Docker 17.06+ CE**. 
The current Docker version used for this project is **Docker 20.10.22 CE**. 
I recommend Docker Stable, but Docker Edge should work as well.

**NOTE:** Switching between Docker Stable and Docker Edge will remove all images and
settings.  Don't forget to restore your memory setting and be prepared to
provision.

**NOTE:** This project is provisioned for Linux and Mac OS only.

For macOS users, please use `Docker for Mac`_. Previous Mac-based tools (e.g.
boot2docker) are *not* supported. 


Note
~~~~~~~~~~~~~

1. You should run all ``make`` commands described below on your local machinge, *not*
from within a Virtual Machine, as these commands are meant to stand up a VM-like environment using
Docker containers.
2. Ensure to append ``sudo`` to all commands if your Docker permission configs is not properly set
Or if you always require sudo to execute docker commands 

Directions to setup
~~~~~~~~~~~~~

Clone this project or download the zip file. You may also run online with ``Gitpod`` alternatively- 
Get Gitpod here - https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki

Clone the project
~~~~~~~~~~~~~~~~~

   .. code:: sh

        git clone https://github.com/otuozeAhmed/akkodis.git

not: open the the folder in a text editor or cd into it (akkodis) 

Buid and start the containers.
~~~~~~~~~~~~~

   .. code:: sh

        make start

Password Generator.
~~~~~~~~~~~~~

   .. code:: sh

       make password.generate

Process Monitor.
~~~~~~~~~~~~~

   .. code:: sh

       make process.monitor

note: process data is populated real-time in data.json
 
Contact Book.
~~~~~~~~~~~~~
   .. code:: sh

       make contact.book

note: contact data is stored in contacts.sqlite3 automatically

