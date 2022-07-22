# ©Copyright ItzVouzz - 2022. All Rights Reserved
# Tool By ItzVouzz

import random

print("\nRANDOM PASSWORD GENERATOR\nBy ItzVouzz\n")

password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','/','[',']','=','+','_','-','!','@','#','$','%','^','&','*','(',')','`','~','?',',','"',"'",':',';','{','}']

passwordLength = input("[-] How much length of password do you want? ")
try:
    int(passwordLength)
except:
    print("\n[!] Password length must be number\n")
    exit()

totalPassword = input("[-] How many random passwords do you want? ")
try:
    int(totalPassword)
except:
    print("\n[!] Total random password must be number\n")
    exit()

passwordLength = int(passwordLength)
totalPassword = int(totalPassword)
print("")
i = 0
while(i < totalPassword):
    random_password = random.choices(password, k = passwordLength)
    random_password = "".join(random_password)
    print(random_password)
    print("")
    i += 1
print("THANKS FOR USING MY TOOL\n©Copyright ItzVouzz - 2022\n")