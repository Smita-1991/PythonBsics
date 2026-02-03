# with open('text.txt') as file:   #### No need to write the close()
# ###Read the file
#     print(file.read())
#
# ####Read n number of character by passing the character
#     print(file.read(2))  ##ab
#
# ###Read one single line at the time of readline
#     print(file.readline())
#
# ###print all the content linebyline by using the readline()
#
# ####By using readline()
#     line=file.readline()
#     while line!="":
#         print(line.strip())
#         line=file.readline()
#
# ###By using readline()
#     lines=file.readlines()
#     for line in lines:
#         print(line.strip())


####Read the file and store all the lines into the list
####Reverse the list
####Write the list back to the file
with open('text.txt', 'r') as file:

    lines= file.readlines()
    # reversed_lines = []
    # lenLines = len(lines)
    # while lenLines>=1:
    #     reversed_lines.append(lines[lenLines-1])
    #     lenLines = lenLines - 1

    with open('text.txt', 'w') as file:
        for line in reversed(lines):  ### reversed(lines) is used to reverse the list
            file.write(line)