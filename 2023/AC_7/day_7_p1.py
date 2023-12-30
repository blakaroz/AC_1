
cards= "23456789TJQKA"

def strength(hand):
    #counts = [hand.count(card) for card in hand]
    counts = []
    for card in hand:
        counts.append(hand.count(card))
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def order(hand):
    return (strength(hand), [cards.index(card) for card in hand])

plays = []

with open("input.txt") as file:
    lines = file.read().split("\n")
    for line in lines:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

    

plays.sort(key=lambda play: order(play[0]))

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)