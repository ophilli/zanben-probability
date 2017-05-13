# [Quora Background Info](https://www.quora.com/Three-cards-are-pulled-from-a-deck-of-52-cards-What-is-the-probability-of-getting-at-least-one-club)

from scipy.special import comb

def probFunc(deckSize, numCardsInCategory, numDraws):
    """
    Sums the combinations of all favorable events to calculate the probability
    of drawing at least one card in the category from the deck
    """

    possibleEvents = comb(deckSize, numDraws)
    favorableEvents = 0

    if(numDraws <= 0):
        return 0
    if(numDraws == 1):
        possibleEvents = deckSize
        favorableEvents = numCardsInCategory

    else:
        for draws in range(numDraws):
            favorableEvents += comb(numCardsInCategory, draws+1) \
                * comb(deckSize - numCardsInCategory, numDraws - draws - 1)


    return favorableEvents / possibleEvents

def probFromZero(deckSize, numCardsInCategory, numDraws):
    """
    Calculates the probability of drawing at least one card in the category from the deck
    ---
    This does the same thing as probFunc(), just in a simpler way
    """

    possibleEvents = comb(deckSize, numDraws)
    zeroEvents = comb(deckSize-numCardsInCategory, numDraws)

    return 1 - (zeroEvents / possibleEvents)

if __name__ == "__main__":
    for x in range(0,53):
        print(str(x) + ": " + str(probFromZero(52,4,x)))
