def findNeedle(haystack):
    index = haystack.index("needle")
   # return index
    return f"found the needle at position {index}"

haystack = ['junk', 'hay', 'more junk', 'shovel', 'needle', 'random stuff']
print(findNeedle(haystack))

