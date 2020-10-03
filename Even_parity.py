import time

#Time complexity O(n)
def even_parity_1(x):
    start_time = time.perf_counter()
    result = 0
    while(x):
        result ^= x & 1
        x >>= 1
    print("Time complexity o(n) :",time.perf_counter()-start_time,"seconds")
    return result

#Time complexity O(k) 
#where K is the number of set bit
def even_parity_2(x):
    start_time = time.perf_counter()
    result = 0
    while x:
        result ^= 1
        x &= x-1  #drops the lowest set bit
    print("Time complexity o(k) :",time.perf_counter()-start_time,"seconds")
    return result

#Time complexity is O(log n)
#where n is the word size
def even_parity_3(x):
    start_time = time.perf_counter()
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    print("Time complexity o(log n) :",time.perf_counter()-start_time,"seconds")
    return x&0x1 #to extract only the last bit

even_parity_1(3)
even_parity_2(3)
even_parity_3(3)


