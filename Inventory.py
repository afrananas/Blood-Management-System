from database import *
class Inventory:

    @staticmethod

    def add_blood(blood_type,quantity=1):
        query = f"""SELECT quantity from inventory WHERE 
        blood_type = '{blood_type}';"""
        result = db_query(query)[0][0]
        result = result + quantity
        query = f"""UPDATE inventory SET quantity = {result} WHERE 
               blood_type= '{blood_type}';
        """
        db_query(query)
        db.commit()

    @staticmethod
    def deduced_blood(blood_type,quantity=1):
        query = f"""SELECT quantity from inventory WHERE 
                blood_type = '{blood_type}';"""
        result = db_query(query)[0][0]

        if result < quantity:
            print("Sorry, Not sufficient blood available.")
        else:
            result = result - quantity
            query = f"""UPDATE inventory SET quantity = {result} WHERE 
                           blood_type= '{blood_type}';
                    """
            db_query(query)
            db.commit()


# Inventory.add_blood("A+",20)