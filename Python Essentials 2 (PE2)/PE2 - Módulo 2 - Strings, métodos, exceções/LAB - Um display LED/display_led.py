# LAB: Um display LED

display = ["" for i in range(9)]

display[1] = "#\n#\n#\n#\n#"
display[2] = "###\n  #\n###\n#  \n###"
str = display[1] + display[2]
print(str, end='')
