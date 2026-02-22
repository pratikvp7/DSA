

def first_non_repeating_char_in_string(string):
    for s in string:
        count = 0
        for s1 in string:
            if s == s1:
                count += 1
        if count == 1:
            return s


if __name__ == "__main__":
    print(first_non_repeating_char_in_string("aassfffaasthbvc"))
