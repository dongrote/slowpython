#!/usr/bin/env python
import time


maxval = 2**26

def foo(s, i):
    return (s ^ (i-1))

start = time.time()
s = 0
for i in xrange(0,maxval):
    s = foo(s, i)

print s
end = time.time()
function_delta = end - start

start = time.time()
s = 0
for i in xrange(0,maxval):
    s = (s ^ (i-1))

print s
end = time.time()
no_function_delta = end - start

print "Time using a function call: % 10f seconds" % function_delta
print "Time without a function:    % 10f seconds" % no_function_delta
