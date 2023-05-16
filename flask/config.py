import os
# setting the configuration for the sql database for further use in sqlalchemy.
basedir=os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
