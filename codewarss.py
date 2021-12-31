def vowel_count(sentence):

    return sum([list("aeiou").count(i) for i in sentence if i in list("aeiou")])


def friend(x):

    return [i for i in x if len(i) == 4 ]

f = friend(["Ryan","123","Cool Man"])






def to_cc(s):
    s = s.replace("_","-").split("-")

    for i,v in enumerate(s):
        if i == 0:
            continue
        s[i] = s[i].capitalize()
    
    return "".join(s)

print(to_cc("hello_guys"))
