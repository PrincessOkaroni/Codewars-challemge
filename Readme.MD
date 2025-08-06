Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 4" 

### Pseudocode
FUNCTION findNeedle(haystack)
    SET index TO the position of "needle" in haystack
    RETURN "found the needle at position " + index
END FUNCTION

# Example usage:
haystack = ['junk', 'hay', 'more junk', 'shovel', 'needle', 'random stuff']
PRINT findNeedle(haystack)
