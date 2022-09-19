print("Hello, am numbr magician!")
print("Gif 3 indiviual numbr, i show magic")
first = float(input())
print("Ah", first, "Kool Numbr, ANOTHER!")
second = float(input())
print(second, "Very good, very nice, NOW GIF LAST NUMBR")
third = float(input())
if (first == second):
    print("I SAID INDIVIDUAL NUMBRS,", first, "AND", second, "ARE THE SAME NUMBR!")
elif (first != second):
    if (first == third):
        print("I SAID INDIVIDUAL NUMBRS,", first, "AND", third, "ARE THE SAME NUMBR!")
    elif (first != third):
        if (second == third):
            print("I SAID INDIVIDUAL NUMBRS,", second, "AND", third, "ARE THE SAME NUMBR!")
        elif (second != third):
            if (first>second) and (first>third):
                print("Hmm..", first, "Is the biggest number!")
            elif (first<second)