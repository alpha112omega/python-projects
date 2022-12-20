age=int(input("enter age to continue :"))
if(age<0 or age==0 or age>100):
 print("wrong age try again")
elif(age>0 and age<18 or age==18):
 print("child")
elif(age>18 and age<30 or age==30):
 print("boy")
elif(age>31 and age<40 or age==40):
 print("adult")
elif(age>41 and age<60 or age==60):
 print("Men")
elif(age>60  or age<100 and age==100):
 print("old")

 





