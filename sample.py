def verify_user(username, password):
	return True

def login_menu():
	username=  input("enter username:")
	password = input("Enter password:")	
	return username, password	
## connect with db checks username and password
if verify_user(username,password):
		print("1. data services\n2.message services\n3.services")
		opt = input("enter an option:")
else:
	print("Invalid inputs. login agian")
	print("1.login\n2.quit")
	opt = input("enter an option:")
	if opt=="1":
		username,password = login_menu()