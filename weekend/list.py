numbers = [10,12,15,22,25,30,35,40,45]

for i in range(len(numbers)):
    while numbers[i] % 2 == 0:
        print(f"{numbers[i]} is even, dividing by 2")
        break