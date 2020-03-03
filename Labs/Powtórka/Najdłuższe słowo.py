def find_longest_word(word):
    a = 0
    answear = ''
    lst = word.split(" ")
    for i in lst:
        if len(i) > a:
            a = len(i)
            answear = i
    return a, answear






print(find_longest_word("I find your lack of faith disturbing"))