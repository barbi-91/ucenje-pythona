broj = 0
numbers = []
def brojac():
    while broj < 6:
        print(f"At the top i is {broj}")
        numbers.append(broj)

        broj = broj + 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {broj}")

brojac()
print("The nmbers:")
for num in numbers:
    print(num)
