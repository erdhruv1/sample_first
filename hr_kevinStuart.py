def minion_game(string):
    vowels = "AEIOU"

    kevin_score = 0
    stuart_score = 0

    for i in range(len(string)):

        score_to_add = (len(string) - i)

        if string[i] in vowels:
            kevin_score = kevin_score + score_to_add
        else:
            stuart_score = stuart_score + score_to_add

    if kevin_score > stuart_score:
        print("Kevin {0}".format(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart {0}".format(stuart_score))
    else:
        print("Draw")


if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)