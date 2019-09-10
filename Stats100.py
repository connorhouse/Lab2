a = 0
for First100EvenSum in range(0,201,2):
    a = a + First100EvenSum
print(a)

b = 0
for First50OddSum in range(1,100,2):
    b = b + First50OddSum
print(b)

c = 0
for First100Avg in range(1,200,2):
    c = c + First100Avg
c = c/100
print(c)



                # Create a file called Stats100.py. Create functions to complete the following:
                # 2.8 Compute the sum of the first 100 even numbers. Call the function First100EvenSum.
                # 2.9 Compute the sum of the first 50 odd numbers. Call the function First50OddSum.
                # 2.10 Compute the average of the first 100 odd numbers. Call the function First100Avg.