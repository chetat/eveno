# Eveno
Eveno is an event booking app the helps users organize events in different location around the world. Users can View or get registered to an event in a choosen location.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. 
- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `eveno` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:


```bash
export FLASK_APP=run.py 
export FLASK_ENV=development //To run the app in debugging mode 
```

## Roles and Permissions:
### Administrator
- Can View all events and Update **events**
- Can create, view, update and delete **event types**.
- Can view all **tickets** bought by users

### User
- Can create, view, update or delete **events**
- Can view **event types**
- Can create, and view **tickets**

## Endpoints
- Base URL: **eveno.herokuapp.com/api/v1/**

**Note:** All endpoints requires Bearer token. JWT tokens are found in **token.txt** file in the root directory of this project

**Documentation** :https://documenter.getpostman.com/view/6911460/Szt79Vv7?version=latest
## Author
- Yeku Wilfred Chetat
