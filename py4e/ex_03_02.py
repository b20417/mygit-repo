#print ("PY4E")
hrs = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Please enter numeric input")
if fh > 40:
    reg = fr*fh
    otp = (fh-40) * (fr*0.5)
    xp = reg+otp
else:
    xp = fh*fr
print("Pay:",xp)
print("All Done")
