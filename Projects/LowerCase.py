import string
#importing string to use ascii_lowercase
data = "You can have data without information, but you cannot have information without data."
data = data.lower() 

dct = {i: 0 for i in string.ascii_lowercase}
dct = {letter : 0 for letter in string.ascii_lowercase}
#ive been looking for possible work,ive set up the "letter" as possbile word for my loop

for letter in data:
  if letter in dct.keys():
    dct[letter] += 1
#used .keys() method to return into keys
if letter in data != 0:
  print(dct)


#I have issues in understanding the sample code, took me more than an hour to problem solve an issue.
#I look for certain tricks to find ways to code it in simpler form rather than typing each letter of the alphabet manually.
#I feel like this turned out as required by the output