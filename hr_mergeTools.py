from _collections import OrderedDict
import textwrap

def merge_the_tools(string, k):

    myStr = textwrap.wrap(string, k)

    for i in myStr:
        d = OrderedDict.fromkeys(i)
        print(''.join(d))

if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)