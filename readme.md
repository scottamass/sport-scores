Welcome to low spec sports 
a sports and scores webapp that should in theory* run on netscape navigator 2.0 

to be able to run the app on your local machine you will need poetry installed 

from there clone the repo on to your local machine and in your console run 
```bash
$ poetry install
```
this will  install all the depandancys for youy

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```
from there if to run the server on your local machine 
```bash
$ poetry run flask run
```