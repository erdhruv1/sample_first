def wrapItUp(func):

    def inner():
        print("I am a wrapper")
        func()

    return inner

@wrapItUp
def gift():
    print("I am the main gift")


gift()
