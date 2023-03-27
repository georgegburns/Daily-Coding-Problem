# This problem was asked by Facebook.
# Given a function f, and N return a debounced f of N milliseconds.
# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.


import time

def test():
    print('Hello World')
    
def debounced(function, n : int):
    st = time.time()
    time.sleep((n-1)/1000)
    ed = time.time()
    elapse = ed - st
    elapse = round(elapse, 3)
    function
    print(f'It took {elapse} seconds for {function} to be called.')
    
debounced(test, 1)