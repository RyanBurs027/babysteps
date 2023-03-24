import re 
while True:
    
    name = input("Hi, please enter your name: ")
    
    email_add = input("Now please, enter your email adress: ")
    
    if re.match(r'^[a-zA-Z\s@1234567890]+.com$', email_add):
    
        print(f'Hi {name}! We will be contacting you shortly at\n {email_add}')
        break

    else:
        print("hmm seems like you didnt type your email right ")
        continue  