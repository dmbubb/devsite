from random import *

''' find me at http://mbubb.devio.us/python_class/randomDN.py
    https://repl.it/E8nD/18
'''

''' STEP 1: read this code, think about it, and then try it '''
numOf = 10
a = 3
z = 10000
#
def nums():
    for _ in range(numOf):
        print(randint(a, z))

''' STEP 2:
 Finish this function so it returns a randomly chosen
 element of the list L.
'''
def randElt(L):
    pass

''' Here are some lists you can use to test your function '''
nouns = ['pizza', 'pom-pom', 'boy', 'car', 'dad', 'fan', 'hat', 'map', 'pie', 'sun', 'arm', 'chin', 'corn', 'crib', 'fang ', 'game', 'hose', 'maid', 'meal', 'name', 'pencil', 'rock', 'shoe', 'snake', 'step', 'summer', 'tent', 'water', 'alarm', 'bath', 'boot', 'chicken', 'doctor', 'family', 'frog', 'grape', 'jam', 'lock', 'notebook', 'plot', 'sail', 'song', 'spy', 'trail', 'uncle', 'wheel', 'actor', 'beef', 'butter ', 'cherry', 'eggnog', 'gate', 'grain', 'hot', 'oatmeal', 'popcorn', 'rainstorm', 'sugar', 'wood', 'apple', 'battle', 'branch', 'cattle', 'coast', 'drug', 'flock', 'giraffe', 'icicle', 'lace', 'north', 'poison', 'sheet', 'smoke', 'throne', 'vacation', 'able', 'aftermath', 'beginner', 'breakfast', 'caption', 'creator', 'friction', 'guitar', 'laborer', 'lumber', 'mountain', 'picture', 'police', 'route', 'suit', 'thread', 'wealth', 'writer']
adjs = ['aback', 'abrupt', 'aching', 'admirable', 'ahead', 'ambitious', 'annual', 'artistic', 'avaricious', 'basic', 'big', 'blond', 'bountiful', 'bruised', 'canine', 'cheeky', 'clear-cut', 'combative', 'constant', 'cowardly', 'cultivated', 'dangerous', 'deceitful', 'delicate', 'detailed', 'dirty', 'distorted', 'dramatic', 'earsplitting', 'electric', 'energetic', 'ethereal', 'exclusive', 'faded', 'far-off', 'feminine', 'flagrant', 'foamy', 'frail', 'frizzy', 'future', 'ghastly', 'glossy', 'grave', 'grouchy', 'hairy', 'harmful', 'helpful', 'homely', 'humorous', 'idle', 'impartial', 'incandescent', 'inferior', 'interesting', 'jazzy', 'junior', 'kosher', 'lazy', 'likely', 'long', 'lumbering', 'magical', 'materialistic', 'menacing', 'miserable', 'moral', 'mysterious', 'neglected', 'noisy', 'numerous', 'occasional', 'optimal', 'outrageous', 'panicky', 'periodic', 'piercing', 'plush', 'powerful', 'prize', 'puny', 'querulous', 'rambunctious', 'recondite', 'required', 'ritzy', 'rundown', 'satisfying', 'screeching', 'serpentine', 'shocking', 'sincere', 'small', 'soft', 'special', 'spry', 'stark', 'strict', 'subtle', 'surprised', 'tall', 'teeny-tiny', 'these', 'thundering', 'tragic', 'trusting', 'unarmed', 'unfolded', 'unrealistic', 'unwitting', 'uttermost', 'verdant', 'vivacious', 'warmhearted', 'weird', 'white', 'wistful', 'worst']
colors = ["blue", "green", "yellow", "orange", "red", "purple", "gray", "brown"]
verbs = ['accepted', 'achieved', 'added', 'admired', 'admitted', 'adopted', 'advised', 'agreed', 'allowed', 'announced', 'appreciated', 'approved', 'argued', 'arrived', 'asked', 'assisted', 'attacked', 'baked', 'begged', 'behaved', 'boiled', 'borrowed', 'brushed', 'buried', 'called', 'challenged', 'changed', 'chased', 'cheated', 'cheered', 'chewed', 'clapped', 'cleaned', 'collected', 'compared', 'complained', 'confessed', 'constructed', 'controlled', 'copied', 'counted', 'created', 'cried', 'cycled', 'damaged', 'danced', 'delivered', 'destroyed', 'divided', 'dragged', 'earned', 'employed', 'encouraged', 'enjoyed', 'established', 'estimated', 'exercised', 'expanded', 'explained', 'fried', 'gathered', 'greeted', 'guessed', 'harassed', 'hated', 'helped', 'hoped', 'identified', 'interrupted', 'introduced', 'irritated', 'joked', 'jumped', 'kicked', 'killed', 'kissed', 'laughed', 'lied', 'liked', 'listened', 'loved', 'married', 'measured', 'moved', 'murdered', 'needed', 'obeyed', 'offended', 'offered', 'opened', 'painted', 'parked', 'phoned', 'picked', 'played', 'prayed', 'printed', 'pulled', 'punched', 'punished', 'purchased', 'pushed', 'questioned', 'raced', 'relaxed', 'remembered', 'replied', 'retired', 'returned', 'rubbed', 'scolded', 'selected', 'smoked', 'snored', 'stared', 'started', 'studied', 'talked', 'thanked', 'travelled', 'troubled', 'typed', 'used', 'visited', 'waited', 'walked', 'wanted', 'warned', 'winked', 'worried', 'yelled']

''' STEP 3:
 Finish the madderlib() function so that it makes random sentences.
 Hint: play with the madlib() function first.
'''

def madlib():
    print("the", adjs[3], nouns[2], verbs[0], colors[4], nouns[0])

def madderlib():
    # ADD CODE HERE so that it randomly picks nouns and verbs
    print("NOT FINISHED")

''' STEP 4:
The following is a function which defines a simple game. It asks you to guess a number in a range
and prompts you until it is correct choice. Notice the "while" loop. It keeps looping until the
condition is true. WHat is the condition?
'''

def game(lownum,highnum):

    the_number = randint(lownum, highnum)
    guess = int(input("Guess a number between " + str(lownum) + " and " + str(highnum) + ": " ))

    while guess != the_number:
        if guess > the_number:
            print(guess, "was too high. Try again.")
        if guess < the_number:
            print(guess, "was too low. Try again.")
        guess = int(input("Guess again: "))

    print(guess, "was the number! You win!")

