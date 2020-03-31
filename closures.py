def make_multiplier(x):
    def multiply(number):
        return x * number

    return multiply

times3 = make_multiplier(3)
times5 = make_multiplier(5)
times7 = make_multiplier(7)
times9 = make_multiplier(9)

print(times3(20))
print(times5(20))
print(times7(20))
print(times9(20))