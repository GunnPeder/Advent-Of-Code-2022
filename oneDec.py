
def get_totals():
    totals = []
    temp = 0

    for number in open("1decemberText.txt").readlines():
        
        if len(number.strip()) > 0:
            temp += int(number)
        else:
            totals.append(temp)
            temp = 0

    return totals

print(f"Maximum amount of calories is: {max(get_totals())}")

totals = get_totals()
totals.sort(reverse=True)
top_three = [totals[i] for i in range(3)]

print(f"The sum of the top three elves is: {sum(top_three)}")