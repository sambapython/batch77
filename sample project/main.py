import sales 
print("1.sales\n2.purchase")
opt = input("Enter an option:")
if opt=="1":
	# print here all sales operations
	print("1.create customer\n2.QUIT")
	sales_opt = input("Enter an option:")
	if sales_opt == "1":
		# call customer_create function
		sales.customer_create()
elif opt=="2":
	# print here all purchase operations.
	pass