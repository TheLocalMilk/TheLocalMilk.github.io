print("Hello i convert kr to euro and steal 2% pls")
print("How many moneys?")
amount = input()
if(float(amount) < float(7.44)):
  print("Poor little thing, you can have your", float(amount)*0.13, "euros back fully")
elif(float(amount) > float(7.44)):
  print("You gets", float(amount)*0.13*0.98, "euro and i steal the rest")
 
