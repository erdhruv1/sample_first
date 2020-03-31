def smart_divide(msg):
    def nested_func(a, b):
        if b == 0:
            print("sorry")
            return
        msg(a, b)
    return nested_func

@smart_divide
def divide(a, b):
    c = a / b
    print(c)
    return c

def main():
    print(divide(2, 4))

if __name__ == "__main__":
    main()