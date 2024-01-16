#welcome
print ("Welcome to Karachi Police Online FIR Registration Portal")
print ('Kindly Fill the Form with Most Accurate Knowledge ')
#user_input
fir_list = []
name_ = input('Enter Your Name:')
fname_ = input('Enter Your Father Name:')
no_ = int(input ('Enter your Mobile Number:'))
cnic_ =int( input ('Enter your CNIC:'))
#crime_input
print ('Crime Incident :')
print ('1.Murder/Rape')
print ("2.Theft/Robbery")
print ('3.Drug/Smuggler')
print ('4.Fraud/Scam')
print ('5.Others')
Crime_ = input('Enter Crime in Words:')
people_ = int(input("Person included in Crime:"))
location_ = input ('Enter Crime Location: ')
date_time = input("Enter date and time (YYYY-MM-DD HH:mm:ss): ")
description_ = input('Give a beief description: ')
suspect_ = input ("Is there any suspect? (yes/no):")
#if_condition
if suspect_ == "yes":
  susdetail_ =input ("Give Suspect Detail:")
elif suspect_ == "no":
  print ("Let us know if you have doubt on someone")
else :
  print ("Invalid Input.Please Enter Yes or No")
witness_ = input ("Is there any witnesses? (yes/no):")
if witness_ == "yes":
  witdetail_ =input ("Give Witness Detail:")
elif witness_ == "no":
  print ("Let us know if you found any.")
else :
  print ("Invalid Input.Please Enter Yes or No")
#adding user_input in new list
new_fir = {
    "name_": name_ ,
    "fname_": fname_ ,
    "no_" :no_ ,
    "cnic_" :cnic_ ,
    "Crime_" :Crime_ ,
    "date_time":date_time,
    "location_" :location_,
    "suspect_": suspect_,
    "witness_": witness_
}

fir_list.append(new_fir)
#final result
print("Name:",name_)
print("Father Name:",fname_)
print("Phone Number:",no_)
print("CNIC :",cnic_)
print("Crime:",Crime_)
print("Date and Time:",date_time)
print("Location:",location_)
print("Suspect:",suspect_)
print("Witness:",witness_)
#correction if made by user
correct_ =input("Is This Information Correct? (yes/no):")
if correct_ == "yes":
  print ("Thankyou For Reporting.Action will be taken on your complaint.Also An Official will soon contact you.")
elif correct_ == "no":
  input ("Enter What have you missed ?.")
else :
  print ("Invalid Input.Please Enter Yes or No")