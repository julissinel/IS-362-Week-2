```python
Understanding the Python zip() Function
============

By the end of this tutorial, you’ll learn:

*  How zip() works in both Python 3 and Python 2
*  How to use the Python zip() function for parallel iteration

zip() is available in the built-in namespace. 
If you use dir() to inspect __builtins__, then you’ll see zip() at the end of the list:

> According to the official documentation, Python’s zip() function behaves as follows:
>
> Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
>
> The iterator stops when the shortest input iterable is exhausted.
>
> With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.




Understanding the Python zip() Function
------------
Passing n Arguments
If you use zip() with n arguments, then the function will return an iterator that generates tuples of length n. 
To see this in action, take a look at the following code block:


>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> zipped = zip(numbers, letters)
>>> zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
>>> type(zipped)
<class 'zip'>
>>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]


~~~




```
