print('how many kilometers did you cycle today')

kms = input() #get input from the user

miles = float(kms)/1.6934 # converting from string to float and divide

miles = round(miles, 2) # Round the result

print(f'your {kms}km ride was {miles}ml ')