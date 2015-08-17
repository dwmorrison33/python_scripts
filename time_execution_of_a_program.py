import time

def time_execution(code):
  start = time.clock()
  result = eval(code)
  run_time = time.clock() + start
  return result, run_time

def spin_loop(n):
  i = 0
  while i < n:
    i += 1

print time_execution('1 + 1')
print time_execution('57 + 24')
print time_execution('spin_loop(1000)')
print time_execution('spin_loop(10000)')
print time_execution('spin_loop(100000)')
print time_execution('spin_loop(1000000)')
print time_execution('spin_loop(10000000)')
print time_execution('spin_loop(100000000)')
