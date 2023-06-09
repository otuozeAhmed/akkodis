Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You will need to have the following installed:

- make - https://www.gnu.org/software/make/
- Docker - https://www.docker.com/products/docker-desktop/
- No third party library used - The Docker build will automatically install Python.

FYI
~~~~~~~~~~~~~
Solutions to the first and second sections (multiple choice) can be
found in section_one.txt and section_two.txt respectively.

Note
~~~~~~~~~~~~~

- This project is provisioned for Linux and Mac OS only.
- Ensure to append ``sudo`` to all commands if your Docker permission configs is not properly set Or if you always require sudo to execute docker commands.
- You should run all ``make`` commands described below on your local machinge, *not* from within a Virtual Machine, as these commands are meant to stand up a VM-like environment using Docker containers.
- This project requires **Docker 17.06+ CE**. The current Docker version used for this project is **Docker 20.10.22 CE**. 
- I recommend Docker Stable, but Docker Edge should work as well.


Clone the project
~~~~~~~~~~~~~~~~~

   .. code:: sh

        git clone https://github.com/otuozeAhmed/akkodis.git

Note: Ensure to cd into the (akkodis) folder before running the upcoming commands

Buid process image
~~~~~~~~~~~~~

   .. code:: sh

        make build.process.image

start the containers.
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

Note: Process data is populated real-time in data.json,
typing in executable path can be daunting and not so user friendly,
so, this solution does not require file/paths/to/executable. 
You can type the executable name alone and the program will
automatically detect the executable path for you.
e.g. you can type "chrome" or "firefox" on prompt 
to monitor each process respectively.
 
Contact Book.
~~~~~~~~~~~~~
   .. code:: sh

       make contact.book

note: contact data is stored in contacts.sqlite3 automatically



