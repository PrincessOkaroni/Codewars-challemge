## Challenge 3
# BDD
- create a dictionary from two lists: keys and values.

- keys and values are of the same length
  keys = ['a','b','c'], values = [1,2,3]
   when createDict(keys,values) is called
   Return{'a':1,'b':2,'c':3}

- more keys than values
keys  = ['a','b','c'], values = [1]
 when createDict(keys,values) is called
 return {'a':1,'b':None,'c':None}

- more values than keys
keys = ['a'], values = [1,2,3]
 when createDict(keys,values) is called
 return{'a':1}(extra values are ignored)

 ## Pseudocode
 - function createDict(keys,values):

    initialize empty dictionary result

    for index from 0 to length of keys

     if index < length of values;

       result[keys[index]]=values[index]

    else:

       result[keys[index]]= None
       
   Return result
