# Given a 32-bit positive integer N, 
# determine whether it is a power of four in faster than O(log N) time.

TEST = 16

def powerofFour(N : int):
    return N and (N & (N - 1)) == 0 and (N & 0x55555555) == N

print(powerofFour(TEST))
        