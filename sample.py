def service_menu():
	print("1. data services\n2.message services\n3.services")
	opt = input("enter an option:")

def primary_menu():
	print("1.login\n2.register")
	opt = input("enter an option:")
	if opt=="1":
		login_menu()
	elif opt=="2":
		register_menu()
def verify_user(username, password):
	return True

def login_menu():
	username=  input("enter username:")
	password = input("Enter password:")	
	
	if verify_user(username,password):
		service_menu()

	else:
		print("Invalid inputs. login agian")
		primary_menu()

primary_menu()