num_columns = int(input("Enter the number of num_columns: "))
#print 1-100 by column
for i in range(1, 100):
    print(f"{i:>3}", end=" ")
    if i % num_columns == 0:
        print()