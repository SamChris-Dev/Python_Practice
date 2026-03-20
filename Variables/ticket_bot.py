age = int(input("Please input your age: "))

if age < 13:
    print("Your ticket cost $8. You are allowed to watch PG movies" )
elif age >= 13 and age <= 17 :
    print("Your ticket cost $12, You can watch PG-13 movies")
elif age >18:
    print("Your ticket cost $15, You can  watch any movie")