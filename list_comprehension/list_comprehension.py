###########   Exxample of List Comprehension with expression & withon any condition   ######
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

#Add 1 in each item of list1 and insert into list2

list2 = []

for i in list1:
    list2.append(i+1)
print(list2)

#### using list comprehension
list3 = [i+1 for i in list1]
print(list3)

########  List Comprehension with expression & condition     ########

list_a = []
for i in range(20):
    if i%2==0 :
        list_a.append(i)
print(list_a)

list_b = [i for i in range(20) if i%2 == 0]
print(list_b)


########  List Comprehension with expression & more than one -condition     ########

list1_a = []
for i in range(20):
    if i%2==0 :
        if i%3==0:
            list1_a.append(i)
print(list1_a)

list1_b = [i for i in range(20) if i%2 == 0 if i%3==0]
print(list1_b)

#################     list comprehension with if-else             ###########################

a = []
for i in range(20):
    if i%2==0 :
        a.append(i)
    else:
        a.append("invalid")
print(a)

b = [i if i%2==0 else "invalid" for i in range(20)]
print(b)

###########   nested list-comprehension      ############3

lis1 = []

for i in range(6,8):
    for j in range(4,7):
        lis1.append(i*j)

print(lis1)

k = [[i*j for j in range(4,7)] for i in range(6,8)]
print(k)