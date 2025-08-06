Feature: Find the needle in a haystack

###I want to find the position of the word "needle" in a list

  After finding the needle, return a message with its index.

  Scenario: Needle is present in the haystack
### Given a haystack= ['junk', 'hay', 'more junk', 'shovel', 'needle', 'random stuff']
    When I search for the needle in our list,
    I should get the output: "found the needle at position 4"
