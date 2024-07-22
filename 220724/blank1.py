print(" *** Multi words *** ")

inp = input("Enter word and number : ")
a, b = inp.split()

multiWords = (a + ' ') * int(b)

print(f"Multiwords : {multiWords}")
