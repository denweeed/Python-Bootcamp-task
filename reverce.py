def reverse(any_string):
    if any_string == "":
        return any_string
    else:
        return reverse(any_string[1:]) + any_string[:1]


if __name__ == "__main__":
    s = "string"
    print(reverse(s))
