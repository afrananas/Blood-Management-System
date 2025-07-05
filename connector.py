
from sqlalchemy import create_engine
from getpass import getpass
password = getpass()
engine = create_engine('mysql+pymysql://root{}@localhost/bloodbank'.format(password))

with engine.connect() as conn:
    result = conn.execute('select * from donor;')

offices = list(result)