# A simple text game that predicts your winning chances according to your health status
name = input("Enter your name: ")
health = int(input("In a scale of 1-100, what is your health: "))

if health > 70:
    print(name, ", You are ready for the battle ")
elif health >= 30 and health <= 70:
    print("Damn! ", name, ", it's risky, but you might survive")
elif health < 30:
    print("Run away! You need a potion")