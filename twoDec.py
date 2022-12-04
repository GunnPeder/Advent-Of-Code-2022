
def get_tuples():

    liste = []
    for line in open("2decemberText.txt").readlines():
        line = line.strip().split(" ")
        liste.append((line[0], line[1]))

    return liste

def score_outcomes():

    wins = [('C', 'X'),('A', 'Y'),('B', 'Z')]
    draws = [('A', 'X'),('B', 'Y'),('C', 'Z')]
    return wins, draws

wins, draws = score_outcomes()
own_points = {'X': 1, 'Y': 2, 'Z':3}
score = 0

for opponent, myself in get_tuples():
    if (opponent, myself) in wins:
        score += 6
    elif (opponent, myself) in draws:
        score += 3
  
    score += own_points.get(myself)

print(f"The total score using own algorithm: {score}")

data = [line.strip().replace(' ', '') for line in open('2decemberText.txt', 'r')]

updated_score = sum({'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}[round] for round in data)
print(f"Total sum with updated algorithm is: {updated_score}")