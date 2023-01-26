print ('hello world')

#Running Sum
Total  = 0
while True:
    i = int(input('Enter any number of your choice: '))
    if i >= 0:    
        print(f'The value of Total will be {Total}')
    else:
        print(Total)
    Total += i