lastname = input("Enter the customer's last name: ")
sales = float(input("Enter the sales amount: £"))
commission = sales * 0.15
print()
print("Customer: "+ lastname)
print("Sales: £"+ str(sales))
commission = round(commission, 2)
print("Employee commission: £"+ str(commission))

