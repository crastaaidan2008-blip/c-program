#name  pan card acc no-1000  date of birth
# e-mail id contact number address current balance
my_tuple= ()
my_list= []
name=input("enter your name")
pan=int(input("enter pan card number"))
accountno=int(input("enter your account number"))
dob=int(input("enter date of birth"))
my_tuple=(name,pan,accountno,dob)
my_list.append(my_tuple)
balance=float(input("enter your balance"))
email=(input("enter your email"))
address=(input("enter your address"))
phone=int(input("enter phone number"))
my_list.append(balance)
my_list.append(email)
my_list.append(address)
my_list.append(phone)
