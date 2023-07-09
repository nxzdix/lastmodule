def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
                print(sym, counter)

strcounter('abc')

