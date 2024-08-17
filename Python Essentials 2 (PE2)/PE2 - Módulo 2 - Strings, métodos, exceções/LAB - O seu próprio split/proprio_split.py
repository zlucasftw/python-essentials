# LAB: O seu próprio split


def mysplit(strng):
    #
    # put your code here
    #
    if strng.isspace():
        return strng.split()
    elif len(strng) == 0:
        return strng.split()

    return strng.split()


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
