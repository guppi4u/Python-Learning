
def BetsAndDraw():

    drawn = [5, 11, 9, 42, 3, 49]
    bets = [3, 7, 11, 42, 34, 49]
    hits = 0

    for number in bets:  # check for number in bets 
        if number in drawn:  # check if same number is also present in drawn
            hits += 1 # if matches then increment hits count

    print(hits)  # print number of hits 


def main():
    BetsAndDraw()



main()

