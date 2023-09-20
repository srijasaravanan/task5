age1=int(input("Enter my age"))
age2=int(input("Enter your age"))
if age1 > age2:
  diff = age1 - age2
  if diff == 1:
     print("Iam younger than you")
  else:
     print("Iam older than you")
elif age2 > age1:
  diff= age2 - age1
  if diff == 1:
     print("You are older than me")
  else:
     print("You are younger than me")
else:
   print("we are in equal age")


 