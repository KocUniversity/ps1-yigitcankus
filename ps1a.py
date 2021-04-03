n, B = list(map(int, input().strip().split()))
T = 0

# your code here

p = 0
pxn = 0 
# pxn is the sum of p1^(n-1) + p2^(n-2) .... without T.
# I am taking them into T paranthesis then finding the right T.

for i in range(1,n+1):
  if i%2 == 1:
    p = (3**i) + 1
  else:
    p = (2**i) + 1
  pxn += p**(n-i)
  p = 0

for t in range(1,10001):
  if pxn*t > B:
    T = t
    break

if T == 0:
  T = -1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)