print("Registration\n")
newU=input("Enter New User Name: ")
newP=input("Enter Password: ")
print("Registered Successfully!\n")
checkU=input("Enter Your User name: ")
checkP=input("Enter your Password: ")
if newP==checkP and newU == checkU:
    print("Login Successfully!")
else:
    print("Invalid Credentials\n")
