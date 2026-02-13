sum = 0
for numbers in range(1,1000):
    for j in range(1,numbers//2+1):
        if numbers % j == 0:
            sum += j
        if sum == numbers:
            print("this is a perfect number",sum)

