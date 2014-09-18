# https://www.hackerrank.com/challenges/gem-stones
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Sample Input
# 3
# abcdde
# baccd
# eeabg

# Sample Output
# 2

# read the elements in the first rock. store this in a hash. 
# for each subsequent rock, check to see if each element from the first rock exists
# if it doesn't, remove that element from the hash
# at the very end, what is left in the hash are elements that appeared in all rocks

def gem_elements(list_of_rock_compositions):
    first_rock = list_of_rock_compositions[0]
    gem_elements = set(first_rock)

    for composition in list_of_rock_compositions: 
        for element in gem_elements.copy(): # must iterate over copy of the set, otherwise RuntimeError: Set changed size during iteration
            if element not in composition:
                gem_elements.remove(element)

    return len(gem_elements)

N = int(raw_input()) # number of rocks
rock_list = []
for i in xrange(N):
    rock = raw_input()
    rock_list.append(rock)

print gem_elements(rock_list)

# O(100 * 26) = O(n) ~ constant

