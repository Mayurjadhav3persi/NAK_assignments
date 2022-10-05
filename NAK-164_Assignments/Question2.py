print("Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.",\
"Sample String : 'restart the terminal'",\
"Expected Result : 'resta$t the te$minal'")
def cng_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(cng_char('restart the terminal'))