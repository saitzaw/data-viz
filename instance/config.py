from os import environ 

class Config: 
    SECRETE_KEY=environ.get('SECRETE_KEy')
    FLASK_APP=environ.get('FLASK_APP') 
    FLASK_ENV=environ.get('FLASK_ENV')
