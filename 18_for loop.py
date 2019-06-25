for my_var in "juniper":
    print(my_var)


friends = ["jim", "carren", "kevin"]

for my_var2 in friends:
    print(my_var2)

for my_var3 in range(10):
    print(my_var3)

for my_var4 in range(len(friends)):
    print(friends[my_var4])

for my_var5 in range(len(friends)):
    if my_var5 == 0:
        print("First iteration")
    else:
        print("Not first")