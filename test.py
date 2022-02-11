# Python program to validate an Email 
from tkinter import * 
# import re module 
ll =Tk()
# re module provides support 
# for regular expressions 
import re 
  
# Make a regular expression 
# for validating an Email 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = Entry(ll, width=30)
email.pack()

# Define a function for 
# for validating an Email 
def check():  
     
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email.get())):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email") 

bbtn= Button(ll, text="click", command=check)
bbtn.pack()
ll.mainloop()