str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

def merge_strings_alternately(str1, str2):
    return "".join(
            [str1[i] + str2[i] for i in range(min(len(str1), len(str2)))]
        ) + str1[len(str2):] + str2[len(str1):]

print(merge_strings_alternately(str1, str2))

