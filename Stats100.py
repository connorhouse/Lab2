a = 0
for first100EvenSum in range(0,201,2):
    a = a + first100EvenSum #can use += too
print(a)

b = 0
for first50OddSum in range(1,100,2):
    b = b + first50OddSum #can use += too
print(b)

c = 0
for first100Avg in range(1,200,2):
    c = c + first100Avg #can use += too
c = c/100
print(c)










                # Create a file called Stats100.py. Create functions to complete the following:
                # 2.8 Compute the sum of the first 100 even numbers. Call the function First100EvenSum.
                # 2.9 Compute the sum of the first 50 odd numbers. Call the function First50OddSum.
                # 2.10 Compute the average of the first 100 odd numbers. Call the function First100Avg.