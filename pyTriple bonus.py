function
sideA = input ("Please input a value: ")
sideB = input ("Please input a 2nd value: ")
sideC = input ("Please input a 3rd value: ")

a = int(sideA)

b = int(sideB)

c = int(sideC)

if (a > b) and (a > c):
    hyp = a
    sA = b
    sB = c
elif (b > a) and (b > c):
            hyp = b
            sA = a
            sB = c
else:
            hyp = c
            sA = a
            sB = c

if (hyp ** 2) == ((sA ** 2) + (sB ** 2)):
    print ("Pythagorean Triple")
else:
    print ("Not Pythagorean Triple")

run = input ("try again? y/n")

if run == "y":

elif run == "n":
    exit()
    else
    print ("Invalid input" + run)
