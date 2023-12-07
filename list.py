fruits = ['apple',"banana",'''pineapple''','apple']  # this is tuple to store multiple fruits in one variable



print('Before change')
for fruit in fruits:
    print(f"I like {fruit}")
    

print("After change")
fruits[0] = "Kiwi" # change the value of List
for fruit in fruits:
    print(f"I like {fruit}")