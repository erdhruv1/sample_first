
def func_is_digit

def func_is_alpha(myStr):
    for i in myStr:
        if i.isalpha():
            return True

    return False

def func_is_alnum(myStr):
    return myStr.isalnum()

def main():
    str = 'qA2'

    print(func_is_alnum(str))
    print(func_is_alpha(str))
    print(func_is_digit(str))
    print(func_is_lower(str))
    print(func_is_upper(str))


if __name__ == '__main__':
    main()