a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed" # chr(10) is ASCII for \n and chr(9) is for ' ' (space)
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

 # should not be ended with a \, as it skips the "
error_string = r"this string ends with \\"
