'''
import file1
import file2
print(file1.x)
print(file1.name)
file1.fun1()
file2.fun2()
'''
#import os
#import file3
# import sys
# print(sys.path)
# import file3
# file3.fun3()
'''
import sys
#sys.path.append("C:\\Users\\Lenovo\\OneDrive\\Desktop")
sys.path.insert(0,"C:\\Users\\Lenovo\\OneDrive\\Desktop")
print(sys.path)
import file4
file4.fun4()
'''
#import file5
'''
it look for pyc file in __pycache__ folder, 
1. if the file not there.
	 then it will create it.
2. It find the file.
   it will compare created/modified date and time of .py and .pyc file
    created_modified_date__file.py>created_modified_date_file.pyc: it will create the .pyc file.
    created_modified_date__file.py<created_modified_date_file.pyc: 
    		It will not create the .pyc file.
    		A. there is a chance of creating .pyc again if you run with different version.
    		i.e .pyc file available for 3.8,  but your running main.py with 3.9 version, then it will create the .pyc file
    		B. there is a chance of creating .pyc again if you run with different python compiler
'''
#import accounts
#accounts.payable_accounts.fun()
from accounts import payable_accounts, receivable_accounts
payable_accounts.fun()
receivable_accounts.fun()