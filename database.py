import mysql.connector
from getpass import getpass
password_= getpass()
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="".format(password_),
    database="bloodbank"
)
print(f"connected: {db}")

cursor = db.cursor()

def db_query(query):
    cursor.execute(query)
    return cursor.fetchall()


def create_tables():
    inventory_table = """
        CREATE TABLE IF NOT EXISTS inventory (
            blood_id INT AUTO_INCREMENT PRIMARY KEY,
            blood_type VARCHAR(5) NOT NULL,
            quantity INT NOT NULL
        );
        """

    donor_table = """
        CREATE TABLE IF NOT EXISTS donor (
            donor_id INT AUTO_INCREMENT PRIMARY KEY,
            donor_name VARCHAR(30) NOT NULL,
            donor_age INT NOT NULL,
            donor_blood_type VARCHAR(5) NOT NULL
        );
        """

    request_table = """
        CREATE TABLE IF NOT EXISTS request (
            request_id INT AUTO_INCREMENT PRIMARY KEY,
            hospital_name VARCHAR(30) NOT NULL,
            patient_name VARCHAR(30) NOT NULL,
            patient_age INT NOT NULL,
            patient_blood_type VARCHAR(5) NOT NULL,
            donor_name VARCHAR(30) NOT NULL,
            donor_age INT NOT NULL,
            donor_blood_type VARCHAR(5) NOT NULL
        );
        """

    cursor.execute(donor_table)
    cursor.execute(inventory_table)
    cursor.execute(request_table)
    db.commit()



if __name__ == "__main__":
    create_tables()