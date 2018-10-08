#Question 1

import re
s=input("Enter an E-mail")
m=re.findall('^[0-9A-Za-z][\w_]*[@](gmail.com|yahoo.com)',s)
if m:
    print("Valid email")
else:
    print("Invalid")


#Question 2

import re
s=input("Enter a mobile number with country code")
m=re.findall('^[+]91[6-9][0-9]{9}',s)
if m:
    print("Indian Number")
else:
    print("Not Indian")


