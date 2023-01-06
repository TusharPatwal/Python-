def tushar4(d, ascending=True):
    def sort_key(item):
        return item[0]

    return sorted(d.items(), key=sort_key, reverse=not ascending)

def tushar5(d, ascending=True):
    def sort_value(item):
        return item[1]

    return sorted(d.items(), key=sort_value, reverse=not ascending)

d = {'b': 2, 'a': 1, 'c': 3, 'd': 4, 'e': 5}

print(tushar4(d))  
print(tushar4(d,False))
print(tushar5(d))
print(tushar5(d, False))
