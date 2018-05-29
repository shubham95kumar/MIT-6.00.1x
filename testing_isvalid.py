# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:15:44 2018

@author: Lenovo
"""
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,\
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,\
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    length = len(word)
    score = 0
    for each in word:
        score += SCRABBLE_LETTER_VALUES[each]

    Tscore = length*(score)
    if length == n:
         return Tscore+ 50
    else:
          return Tscore
  


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    Freq = getFrequencyDict(word)
    count = 0
    if len(word)>0:
        try:
            for each in word:
                if Freq[each] <= hand[each] and word in wordList:
                    count += 1
        except KeyError:
            return False
        else:
            if count == len(word):
                return True
            else: 
                return False
    else:
        return False

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    Hand = hand.copy()
    for x in word:
      Hand[x] = Hand[x]-1
    
    print (Hand)
    return Hand

    
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = sum(hand.values())
    return handlen



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    totalScore = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        displayHand(hand)
        
        # Ask user for input
        word = input("Enter word, or a '.' to indicate that you are finished" )
        
        
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again")
                print()
                continue

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totalScore += getWordScore(word, n)
                print(word, "earned",getWordScore(word, n), "points.","Total score:",totalScore,"points" )
                print()
                # Update the hand 
                hand = updateHand(hand, word)
                
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == '.':
        print("Goodbye!", "Total score:", totalScore)
    else:
        print("Run out of letters.", "Total score:", totalScore)
