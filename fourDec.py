

tekst = open("4decemberText.txt").readlines()
tuples = []

for lines in tekst:
    splitted = lines.split(",")
    tuples.append((splitted[0].strip(), splitted[1].strip()))

counter_part1 = 0
counter_part2 = 0

for group1, group2 in tuples:

    group1 = group1.split("-")
    group2 = group2.split("-")

    first_range = [i for i in range(int(group1[0]), int(group1[1])+1)]
    second_range = [i for i in range(int(group2[0]), int(group2[1])+1)]

    if all(elem in first_range for elem in second_range) or all(elem in second_range for elem in first_range):
        counter_part1 += 1
    
    for lot in first_range:
        if lot in second_range:
            counter_part2 += 1
            break

print(f"The number of obsolete groups: {counter_part1}")
print(f"The number of instances where there is an overlap: {counter_part2}")