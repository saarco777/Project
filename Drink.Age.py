"""
put your age, and you will know if you ca go inside
"""
name = input('Hey there.. Whats your name?')  #the user inputs their name
age = input('How old are you?')  #the user inputs their age

if int(age) > 20:
    print('Hey', name, "Welcome inside. Please have a drink")

elif int(age) < 20 and int(age) > 18:
    print('Hey', name, 'Welcome in.. BUT you cannot have a drink!')

elif float(age) < 18:
    print('Sorry', name, "your too young. You CANNOT come inside")