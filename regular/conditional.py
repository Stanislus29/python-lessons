greater = False 

list = [6, 7 ,9, 12, 15, 18 , 21 , 4, 3, 6, 13, 14, 15]

for i in list:
    print (i)
    if i > 10:
        print('condition met' , i)
        greater = True

    while greater:
        print('There is a number greater than 10 in the list')
        greater = False
        break 

