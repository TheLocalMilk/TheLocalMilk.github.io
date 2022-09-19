print("I show u how much it cost to send letter")
print("Please enter how fat your letter is in kg")
weight = float(input())
if (weight > 2):
    print("Nah dawg you aint gonna tell me you are sending a 'letter' that is above 2 kilos skullemojix7")
elif (weight <= 2):
    if(weight > 0.5 ):
        print("Fat package bro, i think that'll be around 60dkk to send")
    elif (weight <= 0.5):
        if(weight > 0.25):
         print("Pretty average package, i think that'll be around 48dkk to send")
        elif (weight <= 0.25):
            if(weight > 0.1):
                print("Damn your package weighs that little? That'll only be 24dkk to send")
            elif(weight <= 0.1):
             if(weight>0):
                  print("Bro your package is barely even visible you alright? Thats only 12dkk my guy")
             elif(weight <= 0):
                print("Actually brain dead, your package cant weigh nothing, actually throwing rn")