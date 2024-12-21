
f=open("worddic.txt", "r")
dicL=f.read().splitlines()


def longest():
    print(max(dicL, key=len))

def palindromes_six():
    for i in dicL:
        if len(i) > 5 and i==i[::-1]:
            print(i)

def descending():
    for i in reversed(dicL):
        if len(i) > 24:
            print(i)

def ascending_letters():
    for i in dicL:
        string=list(i)
        # print(string)
        sorted_string=sorted(string)
        # print(sorted_string)
        if len(i)>5 and string==sorted_string:
            print(i)

def strict():
    for i in dicL:
        string=list(i)
        # print(string)
        sorted_string=sorted(string)
        # print(sorted_string)
        if len(i)>5 and string==sorted_string:
            for x in sorted_string:
                if string.count(x)>1:
                    break
            else:
                print(i)


# longest()
# palindromes_six()
# descending()
# ascending_letters()
# strict()