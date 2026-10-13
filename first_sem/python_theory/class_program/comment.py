# create a single student data 
# name roll number moblie number email id 
# file subject marks  and get the subject total 
# must be implimented using nested list 
def readData():
    list[[]]
    name=input("enter your name:")
    roll_number=int(input("enter your roll  number:"))
    email_id=(input("enter you email:"))
    phone=int(input("enter phone number:"))
    sub1=int(input("enter sub1 mark:"))
    sub2=int(input("enter sub2 marks:"))
    sub3=int(input("enter sub3 marks:"))
    sub4=int(input("enter sub4 marks:"))
    sub5=int(input("enter su5 marks:"))
    list.append(name)
    list.append(roll_number)
    list.append(email_id)
    list.append(phone)
    list.append(sub1)
    list.append(sub2)
    list.append(sub3)
    list.append(sub4)
    list.append(sub5)
    return list
def total_marks(sub1,sub2,sub3,sub4,sub5):
    total=(sub1+sub2+sub3+sub4+sub5)
    return total
 