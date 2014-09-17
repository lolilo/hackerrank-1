# https://www.hackerrank.com/challenges/utopian-tree

# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle of the tree occurs during the monsoon, when it doubles in height. The second growth cycle of the tree occurs during the summer, when its height increases by 1 meter. 
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. 
# Can you find the height of the tree after N growth cycles?


# start cycle at monsoon, x2 
# increase height accordingly for N cycles, alternating between x2 and + 1 meter

# takes in a function and returns the function memoized
# bahhh, the way I implement it right now doesn't do anything. 
# look into this later......
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def return_tree_height(n):
    cycle = 0
    height = 1 # height is inialized at 1 meter
    
    # if n == cycle: # if n == 0
    #     return height # how to make code more general to account for this case, n == 0?

    while cycle < n: # edge case: if cycle == 0, height = 1
        if cycle % 2 == 0: # if even, it's moonsoon season
            height *= 2
        else: # cycle is odd
            height += 1 
        cycle += 1

    return height

# we can memoize this to make it faster for subsequent calculations...maybe?
def print_tree_heights(test_cases_n):
    for n in test_cases_n:
        print return_tree_height(n)


T = int(raw_input()) # get T, number of test cases

# get a list of T test cases
i = 0
test_cases_n = []
while i < T:
    n = int(raw_input())
    test_cases_n.append(n)
    i += 1

print_tree_heights(test_cases_n)

