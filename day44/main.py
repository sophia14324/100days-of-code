import os
import math
import random
import smtplib

digits = "0123456789"

# Initialize an empty string to store the OTP
OTP = ""

# Generate a 6-digit OTP using random digits
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP + " is your OTP"
msg = otp

# Connect to the Gmail SMTP server
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

# Login to your Gmail account using app password
s.login("Your Gmail Account", "Your app password")

emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input("Enter Your OTP >>: ")

# Check if the entered OTP matches the generated OTP
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
