# QR Confetti

## Overview

This is a lightweight QR code generator web app built using Python Flask and deployed on EC2.

These instructions aren't quite finished, but they should be relatively soon.

## Installation and Usage

There are a few finicky extra steps to get it deployed in a "production" environment (with quotes because it's genuinely only a few files at most), but the process for running it locally is pretty simple.

Start by cloning the repo:

```git clone https://github.com/dustin-ctg/qrconfetti.git```

To install dependencies, ensure you have `pip` installed on your system, and run:

```
    cd qrconfetti
    pip install -r requirements.txt
```

Once the dependencies are installed, use the following command to run a local dev environment:

```flask run```

### Installation Requirements

**Required to run:**

- Python 3.12 
- Flask 3.0.0
- Pillow 10.2.0
- qrcode 7.4.2

**Server requirements for a production environment:**

- nginx
- tmux (For running background shell windows, so you can still use your server while running the app)
- gunicorn (Web Server Gateway Interface, or "WSGI")
- certbot (For SSL)
- certbot-nginx
- virtualenv

### Deployment

This was built to be compatible with a t2.micro AWS EC2 instance, but should be able to run on any production WSGI server running nginx or apache, though this tutorial covers setup for a Ubuntu webserver using nginx specifically.

1. Spin up your instance

This instance will just be a basic t2.micro Free Tier instance running Ubuntu. Be sure to create an ssh key for the instance to connect to it from your local machine.

2. Configure firewall settings

We don't want to expose it to HTTP/HTTPS just yet; start with exposing TCP port 22 (SSH), ensuring to only allow your IP address to connect to the instance. If you don't know your IP address, you can use sites like [WhatIsMyIPAddress](https://whatismyipaddress.com/) to find out. 

If you have a VPN, you'll either have to do some finagling wizardry that's outside the scope of this tutorial, or temporarily disable it while we configure the instance.

3. Connect to the instance

Using the ssh key that you made in step 1, connect to the instance: `ssh -i path/to/your/key ubuntu@xxx.xxx.xxx.xxx`

4. Clone the git repo

Clone the git repo by running this command: `git clone https://github.com/dustin-ctg/qrconfetti.git`

5. Install server dependencies

Since we're using Ubuntu, we'll be using the `apt` package manager:

```
    sudo apt-get update
    sudo apt-get install python3 python3-venv tmux gunicorn
```

Install certbot, its nginx extension, and virtualenv, now that we have pip:

```
    sudo pip install certbot certbot-nginx virtualenv
```

Create a virtual environment, as a best practice:

```
    cd qrconfetti
    virtualenv venv
    source venv/bin/activate
```