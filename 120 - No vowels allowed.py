# Write your solution here
def no_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    for item in vowels:
        if item in my_string:
            my_string = my_string.replace(item, "")
    return my_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
