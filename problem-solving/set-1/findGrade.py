
# from tabulate import tabulate

# l = [["Hassan", 75], ["Ali", 65], ["Ahmed", 54]]
# table = tabulate(l, headers=['Name', 'Marks'], tablefmt='orgtbl')
# print(table,"\n")

# print("Enter Marks Obtained in ICE-3105: ")
# mark = int(input())




# if (mark>=80):
#     print("Your Grade is A+ and Grade point is 4.00")
# elif mark>=75 and mark<=79:
#     print("Your Grade is A and Grade point is 3.75")
# elif mark>=70 and mark<=74:
#    print("Your Grade is A- and Grade point is 3.50")
# elif mark>=65 and mark<=69:
#     print("Your Grade is B+ and Grade point is 3.25")
# elif mark>=60 and mark<=64:
#     print("Your Grade is B and Grade point is 3.00")
# elif mark>=55 and mark<=59:
#     print("Your Grade is B- and Grade point is 2.75")
# else:
#     print("failed")
from tabulate import tabulate 
myData=[
    ["1811001","Rabia",80],
    ["1811007","Rashed",50],
    ["1811034","Adity",30],
    ["1811030","Khalid",60]
]
head=["Roll","Name","Number"]
print(tabulate(myData, headers=head, tablefmt="grid"))

for i in range(4):
    if (myData[i][2])>= 80:
        print(myData[i][0] + " = A+")
    elif (myData[i][2])>= 70:
        print(myData[i][0] + " = A")
    elif (myData[i][2])>= 60:
        print(myData[i][0] + " = A-")
    elif (myData[i][2])>= 50:
        print(myData[i][0] + " = B")
    elif (myData[i][2])>= 40:
        print(myData[i][0] + " = C")
    elif (myData[i][2])>= 33:
        print(myData[i][0] + " = D")
    else :
        print(myData[i][0] +" = Failed")

