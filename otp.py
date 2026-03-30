import random
#generating the otp
otp = ''
def otp_generator(lenght):

    global otp

    otp = ''
    digit = '0123456789'
    
    for i in range(lenght):
        otp += random.choice(digit)
    print(f"Your OTP is : {otp}")

    user_otp = input('Eneter the OTP : ')

#verification

    if user_otp == otp:
        print("OTP Verified!")
    else:
        print("Invalid OTP!")    

lenght = int(input("Enter the lenght of OTP : "))

if lenght >= 4 and lenght <=10 :
    otp = otp_generator(lenght)

else:
    print("OTP lenght must be greater than four and less than ten!!")    


