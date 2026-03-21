rent = int(input("Enter your hostel/ Room Rent :"))
food = int(input("Enter your amount of Food ordered : "))
electricity_spend = int(input("Enter the total of elecricity spend : "))
charge_per_unit = int(input( "Enter the charge per unit : "))
persons = int(input("Enter the Number of Person living in room/ flat : "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons
print("Each person Will pay = ",output)
