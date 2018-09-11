def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
        return count