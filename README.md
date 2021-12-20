# deploy-linux

This is a simple minimal Flask app. Flask is an application that allows a programmer to quickly create the basic structure of a website and can comprehend a range of extensions that adds functionality as your website grows.    

This particular implementation is deliberately simple and can be used to practice deployments in local environments and to remote servers.  

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

Activating environment and installing dependencies with pip

```
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Configuring Flask development server

```
$ export FLASK_APP=deploy.py
$ export FLASK_ENV=development

# Alternately, you may use the package called python-dotenv (part of the above installation of dependencies) to set environmental variables defined in .env

$ mv .sample-env .env  #rename file .env which flask can see

# in .env file place the FLASK_APP & FLASK_ENV lines from above
```

Start Flask

If your configuration is successful, you can start the Flask development server by typing:

```
$ flask run
```
If all is well, you will see the server start noting "serving Flask app 'deploy.py' (lazy loading)" and "Environment: development".  

You will then be able to access the minimal route provided in this package by opening your browser and entering "http:\\\127.0.0.0:5000".  You will see the text "flask-deploy-linux".
