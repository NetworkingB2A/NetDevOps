
#older way to create threads.
# import threading
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f'sleeping {seconds} second(s)')
#     time.sleep(seconds)
#     print('done sleeping...')

# threads = []

# for _ in range(1,10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# print(threads)
  
# for thread in threads:
#     thread.join()
    


# finish = time.perf_counter()
# print(f'finished in {round(finish-start, 2)} seconds(s)')

#new way to create threads.


import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'done sleeping...{seconds}'
time_seconds = [5,4,3,2,1]

# the best way(might be the only way) to run threads is to use a context handler as shown below.
with concurrent.futures.ThreadPoolExecutor() as executor:
    # This is a list comprehension to run the executor and add the results to the list.
    ''' using the submit method, you are running each function one at a time. in order to run submit on an entire list, you need to do a loop. 
    We accomplished this by writing a list comprehension. we can instead use our map method over a list of values. When using the submit method, 
    we get a future object returned to use. When we use the Map method we get a just the return back from the function. map will return the results in the order 
    they were started. With the as_completed the future object was returned as the thread was completed.
    '''
    results = [executor.submit(do_something, time_second) for time_second in time_seconds]
    # This is to use the as completed method to display the results as a thread it completed.
    for f in concurrent.futures.as_completed(results):
        print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    # This is a list comprehension to run the executor and add the results to the list.
    results = executor.map(do_something, time_seconds)
    # This is to use the as completed method to display the results as a thread it completed.
    for result in results:
        print(result) 


finish = time.perf_counter()
print(f'finished in {round(finish-start, 2)} seconds(s)')

