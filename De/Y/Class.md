"""
The conflict with your students escalates, 
and now they are hiding multiple words in a single word grid. 
Return the location of each word as a list of coordinates.
Letters cannot be reused across words.

grid1 = [
['b', 'a', 'b'],
['y', 't', 'a'],
['x', 'x', 't'],
]

words1_1 = ["by","bat"]

find_word_locations(grid1, words1_1) =>
([(0, 0), (1, 0)],
[(0, 2), (1, 2), (2, 2)])

grid2 =[
['A', 'B', 'A', 'B'],
['B', 'A', 'B', 'A'],
['A', 'B', 'Y', 'B'],
['B', 'Y', 'A', 'A'],
['A', 'B', 'B', 'A'],
]
words2_1 = ['ABABY', 'ABY', 'AAA', 'ABAB', 'BABB']

([(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],
[(1, 1), (1, 2), (2, 2)],
[(3, 2), (3, 3), (4, 3)],
[(0, 2), (0, 3), (1, 3), (2, 3)],
[(3, 0), (4, 0), (4, 1), (4, 2)])

or

([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
[(2, 0), (2, 1), (3, 1)],
[(3, 2), (3, 3), (4, 3)],
[(0, 2), (0, 3), (1, 3), (2, 3)],
[(3, 0), (4, 0), (4, 1), (4, 2)])

or

([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],
[(2, 0), (2, 1), (3, 1)],
[(3, 2), (3, 3), (4, 3)],
[(0, 2), (0, 3), (1, 3), (2, 3)],
[(3, 0), (4, 0), (4, 1), (4, 2)])

words2_2 = ['ABABA', 'ABA', 'BAB', 'BABA', 'ABYB']

([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
[(3, 2), (4, 2), (4, 3)],
[(0, 1), (0, 2), (1, 2)],
[(0, 3), (1, 3), (2, 3), (3, 3)],
[(1, 1), (2, 1), (3, 1), (4, 1)])

or

([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
[(3, 2), (4, 2), (4, 3)],
[(0, 1), (0, 2), (0, 3)],
[(1, 2), (1, 3), (2, 3), (3, 3)],
[(1, 1), (2, 1), (3, 1), (4, 1)])

All Test Cases:
find_word_locations(grid1, words1_1)
find_word_locations(grid2, words2_1)
find_word_locations(grid2, words2_2)

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word
"""


grid1 = [
['b', 'a', 'b'],
['y', 't', 'a'],
['x', 'x', 't'],
]
words1_1 = ['by', 'bat']

grid2 =[
['A', 'B', 'A', 'B'],
['B', 'A', 'B', 'A'],
['A', 'B', 'Y', 'B'],
['B', 'Y', 'A', 'A'],
['A', 'B', 'B', 'A'],
]
words2_1 = ['ABABY', 'ABY', 'AAA', 'ABAB', 'BABB']
words2_2 = ['ABABA', 'ABA', 'BAB', 'BABA', 'ABYB']


"""
# we can go right or go down
# we need to write a function
# to check if we reach the end of the word
# if we reach, return the coordinate
def dfs(grid, currentX, currentY, i, word1, coordinates):
# print(f"{word1[i:]} and {coordinates}")
r = len(grid)
c = len(grid[0])
# try to look into currentX,Y'l left and down to see if it match word[1]
if i == len(word1):

        return coordinates
    # print(f"{word1[i:]}")
    if currentY + 1 < c and grid[currentX][currentY + 1] == word1[i]:
        # print(f"1   {word1[i:]} checking {grid[currentX][currentY + 1]}. {currentX, currentY + 1}")
        res = dfs(grid, currentX, currentY + 1, i + 1, word1, coordinates + [(currentX, currentY + 1)])
        if len(res) > 0:
            return res
    if currentX + 1 < r and grid[currentX + 1][currentY] == word1[i]:
        # print(f"2   {word1[i:]} - {word1[i]} checking {grid[currentX + 1][currentY]} {currentX + 1, currentY }")
        res = dfs(grid, currentX + 1, currentY, i + 1, word1, coordinates + [(currentX + 1, currentY )])
        if len(res) > 0:
            return res
    return []


def find_word_location(grid, word1):
r = len(grid)
c = len(grid[0])
for i in range(r):
for j in range(c):
if grid[i][j] == word1[0]:
coordinates = dfs(grid, i, j, 1, word1, [(i, j)])
if len(coordinates):
return coordinates
return []


print(find_word_location(grid1, word1))
print(find_word_location(grid1, word2))
print(find_word_location(grid1, word3))
print(find_word_location(grid1, word4))
print(find_word_location(grid1, word5))
print(find_word_location(grid1, word6))
print(find_word_location(grid1, word7))
print(find_word_location(grid1, word8))
print(find_word_location(grid2, word9))



"""







"""
def find(words, string1):
# we need to count number of letter in word
counterOfString = getCounter(string1)
for word in words:
counter = getCounter(word)
fail = False
for letter, count in counter.items():
if letter not in counterOfString or counterOfString[letter] < count:
fail = True
break
if not fail:
return word
return "-"

def getCounter(string):
counter = {}
for letter in string:
counter[letter] = counter.get(letter, 0) +  1
return counter

print(find(words, string1))
print(find(words, string2))
print(find(words, string3))
print(find(words, string4))
print(find(words, string5))
print(find(words, string6))
"""