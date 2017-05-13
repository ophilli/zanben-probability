# This program is designed to calculate sample probabilities for use in board
# games. It is based on information from the following quora page
# https://www.quora.com/Three-cards-are-pulled-from-a-deck-of-52-cards-What-is-the-probability-of-getting-at-least-one-club

from scipy.special import comb

def compute(deckSize, numCardsInCategory, numAtLeast, numDraws):
    """
    Sums the combinations of all favorable events to calculate the probability
    of drawing at least one card in the category from the deck
    """

    if(numDraws < numAtLeast):
        return 0
    if(numDraws == numAtLeast):
        possibleEvents = deckSize
        favorableEvents = numCardsInCategory

    else:
        possibleEvents = comb(deckSize, numDraws)
        favorableEvents = 0
        for draws in range(numAtLeast-1,numDraws):
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
    choice = int(input('Specific # of draws (0) or full list (1)'))

    deckSize = int(input('Enter the size of the deck: '))
    numCardsInCategory = int(input('Enter the number of the cards in the category: '))
    numAtLeast = int(input('Enter the number of cards to test for - P(X >= n): '))

    if(choice == 0):
        numDraws = int(input('Enter the number of card draws taken: '))

        print(probFunc(deckSize, numCardsInCategory, numAtLeast, numDraws))


    elif(choice == 1):
        print("Draw | Probability")
        for x in range(0,deckSize+1):
            print(str(x) + ": " + str(probFunc(deckSize,numCardsInCategory,numAtLeast,x)))
