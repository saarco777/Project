"""
this script has a class named employees, and we will get the email address combined by the first and last
name
"""
class employees:

    def __init__(self, first, last, pay):

     self.first = first
     self.last = last
     self.pay = pay
     self.email = first + '.' + last + '@gmail.com'  # connect first + last name and add @gmail..


emp1 = employees('Saar', 'Cohen', 22000)
emp2 = employees('Yossi', 'Cohen', 23000)
emp3 = employees('Liran', 'Cohen', 24000)

print('Hello', emp1.first + '!', 'Your new Email Address is:', emp1.email, end='\n\n')
# getting emp1 1 email address

print('Hello', emp2.first + '!', "Your new Email Address is:", emp2.email, end='\n\n')
# getting user 2 email address

print("Hello", emp3.first + '!', 'Your new Email Address is:', emp3.email, end='\n\n')
# getting user 3 email address
