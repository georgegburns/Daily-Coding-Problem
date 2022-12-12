# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

def job_scheduler(f, n: int):
    import time
    start = time.time_ns() / 1000000
    x = start
    end = start + n
    y = end
    while start < end:
        start = time.time_ns() / 1000000
    time = (y-x)/1000
    return f(), print(f'It took {time} seconds before function {f} was called.')

def f():
    print("Hello World!")
    
#test 1
#job_scheduler(f, 60000)

#test 2
job_scheduler(f, 1000)

