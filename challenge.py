# Challenge 3
def create_dict(keys, values):
    result = {}
    for i in range(len(keys)):
      if i < len(values):
        result[keys[i]]=values[i]
      else:
        result[keys[i]] = None
        
    return result

# Challenge 1 Grasshopper

def greet(name, owner):
    if name == owner :
      return "Hello boss"
    else :
      return "Hello guest"
    
print(greet("Mohamed", "Mohamed"))
#greet(name="Ahmed", owner="Mohamed")


# Challenge 5 Needle
def findNeedle(haystack):
    index = haystack.index("needle")
   # return index
    return f"found the needle at position {index}"   

haystack = ['junk', 'hay', 'more junk', 'shovel', 'needle', 'random stuff']
print(findNeedle(haystack))
