from BloodBank import BloodBank

print("Hello G welcome here\n")

def getbloodtype(num):
    blood_dictionary = {1:"A+",2:"A-",3:"B+",4:"B-",5:"O+",6:"O-",7:"AB+",8:"AB-"}
    return blood_dictionary[num]
try:
    options = int(input("Choose the Available Facilities: \n"
                          "1. Add Donor Details\n"
                          "2. Request Blood :"))

    if options == 1:
          #Add Blood logic
          donor_name = input("Enter Donor Name: ")
          donor_age = int(input("Enter Donor age: "))
          temp1 = int(input("""Choose Blood Type:
          1.A+
          2.A-
          3.B+
          4.B-
          5.O+
          6.O-
          7.AB+
          8.AB- :"""))
          donor_blood_type = getbloodtype(temp1)
          BloodBank.donor_details(donor_name,donor_age,donor_blood_type)

    elif options == 2:
        #Request Blood Logic
        hospital_name = input("Enter Hospital Name: ")
        patient_name = input("Enter Patient Name: ")
        patient_age = int(input("Enter Patient age: "))
        temp2 = int(input("""Choose Patient Blood Type:
          1.A+
          2.A-
          3.B+
          4.B-
          5.O+
          6.O-
          7.AB+
          8.AB- :"""))
        patient_blood_type = getbloodtype(temp2)
        donor_name = input("Enter Donor Name: ")

        donor_age = int(input("Enter Donor age: "))
        temp3 = int(input("""Choose Donor Blood Type:
          1.A+
          2.A-
          3.B+
          4.B-
          5.O+
          6.O-
          7.AB+
          8.AB- :"""))
        donor_blood_type = getbloodtype(temp3)
        BloodBank.request_blood(hospital_name,patient_name,patient_age,patient_blood_type,donor_name,donor_age,donor_blood_type)

    else:
        print("Enter a valid Input")
except Exception as e:
      print("Please Enter a Number")

#danis ibee
#travers danis ibee
#code with harry

