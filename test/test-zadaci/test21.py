def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def muliply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a / b


print("lets do some math with just function")

age = add(30,5)
height = subtract(78, 4)
weight = muliply(1,1)
iq = divide (34,100)

print(f"age: {age}, height: {height}, weight:{weight}, iq: {iq}")

print("here is puzzle")
what = add(age, subtract (height, muliply(weight, divide(iq, 2 ))))
print("THAT BECOMES:", what, "can you do it by hand")
