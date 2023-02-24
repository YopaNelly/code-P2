def function(Yo):
    sum = 0
    Yo = Yo.split(",")
    print(Yo)
    for i in Yo:
        sum += int(i)
    return sum


Yo = "56,24,45,2574,1445,556"
print("The sum is: ", function(Yo))
