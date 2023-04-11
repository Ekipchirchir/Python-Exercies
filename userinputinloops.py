def get_number():
    while True:
    x:int(input("Enter the value of x ?"))
    if x < 0:
        break
    return x

def helloworld(n):
    for _ in range(n):
        print("Hello World")
