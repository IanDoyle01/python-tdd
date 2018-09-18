def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
        
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "1 upper case"
assert count_upper_case("a") == 0, "1 lower case"
assert count_upper_case("£$%%^") == 0, "Special Characters"
assert count_upper_case("AaAB") == 3, "3 upper and 1 lower case"
assert count_upper_case("A£$bC") == 2, "2 upper with lower case and special chars"
print("All the tests passed")
