
def get_prios():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enums = enumerate(letters, start=1)
    return enums

dictionary = {}
for (prio, letter) in [x for x in get_prios()]:
    dictionary[letter] = prio


def get_codes():
    tekst = open("3desemberTekst.txt").readlines()
    tekst = [lines.strip() for lines in tekst]
    return tekst

total_sum = 0

for string in get_codes():
    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
    common_letter = ""
    for letter in firstpart:
        if letter in secondpart:
            total_sum += dictionary[letter]
            break

print(f"The total priority sum is: {total_sum}")
            


