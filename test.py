import random
boolean = bool(random.randint(0,1))
print(boolean)

string1 = "hello"
string2 = "world"

print(string1 + " " + string2)

equal = 2 + 2 + 2 
print(equal)


string = "abcdefghijklmnopqrstuvwxyz"

substring = string[11:16]   # => "lmnop"
substring2 = string[:4]     # => "abcd"
substring3 = string[22:]    # => "wxyz"
substring4 = string[-3:]    # => "xyz"

substring5 = string[::2]    # => "acegikmoqsuwy" (every second character)
substring6 = string[::-1]   # => "zyxwvutsrqponmlkjihgfedcba" (reversed string)
substring7 = string[1:8:2]  # => "bdfh" (every second character from index 1 to 7)
hello = "hello"
Hello = hello.capitalize()
print(Hello)