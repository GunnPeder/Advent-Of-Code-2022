
def get_totals():
    totals = []
    temp = 0
    for tall in open("1desemberTekst.txt").readlines():
    
        if len(tall.strip()) > 0:
            temp += int(tall)
        else:
            totals.append(temp)
            temp = 0

    return totals

print(f"maksimalt antall kalorier er: {max(get_totals())}")


totals = get_totals()

totals.sort(reverse=True)

print(totals)

top_three = [totals[i] for i in range(3)]
print(f"The sum of the top three elves is: {sum(top_three)}")