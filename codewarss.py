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

def duplicate_encoder(word):

    return "".join(["(" if word.lower().count(i) < 2 else ")" for i in word.lower() ])


def to_cc2(text):
    text = text.replace("_","-").split("-")
    return "".join(text[0] + i.title() for i in text[1::])


def make_readable(seconds):
    m,s = divmod(seconds,60)
    h,m = divmod(m, 60)

    return f'{h:02d}:{m:02d}:{s:02d}'


def zero_two_d(num1,num2):

    return f'{num1:02d}:{num2:02d}'

print(zero_two_d(0,0))