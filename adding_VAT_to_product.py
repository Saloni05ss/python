print("Enter VAT percentage")
VAT=input()
print("Enter product name")
Name=input()
print("Enter net price of "+ Name)
netPrice=input()
calculatedVAT=(1+int(VAT)/100)
grossPrice=str(int(netPrice)*calculatedVAT)
print("Gross price of "+ Name +" is :" +grossPrice)
