

def remove_duplicate_char_from_string(string):
    s2 = ""
    for s in string:
        if s not in s2:
            s2 = s2 + s
    return s2


if __name__ == '__main__':
    print(remove_duplicate_char_from_string("qw3ertgfdqw3rtyh"))
