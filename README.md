# deploy-linux

This is a simple minimal flask app.

It can be used to practice deployments.

## Install Manual Ubuntu/Bash

Clone this repo to a directory of your choosing. Here we will use /dlinux.

```
$ mkdir dlinux && cd dlinux
$ git clone https://github.com/redmonroe/deploy-linux.git
```

## Configuration

Configuring development environment

```
$ cd deploy-linux
$ python3 -m venv venv

```

Activating environment and Installing dependencies with pip

```
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Configuring Flask development server

```
$ export FLASK_APP=deploy.py
$ export FLASK_ENV=development

Alternately, you may use python-dotenv (part of the above installation of dependencies) to set environmental variables defined in .env

mv .sample-env .env  /rename file .env which flask can see

# in .env file place the FLASK_APP & FLASK_ENV lines from above
```
