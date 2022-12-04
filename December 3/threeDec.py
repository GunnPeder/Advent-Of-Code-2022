
def get_prios():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enums = enumerate(letters, start=1)
    return enums

dictionary = {}
for (prio, letter) in [x for x in get_prios()]:
    dictionary[letter] = prio


def get_codes():
    tekst = open("3decemberText.txt").readlines()
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
            
codes = get_codes()

three_per_chunks = [codes[1:i+3] for i in range(0, len(codes), 3)]

print(three_per_chunks)
