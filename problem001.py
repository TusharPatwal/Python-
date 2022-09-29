# Alice has scored XX marks in her test and Bob has scored YY marks in the same test. Alice is happy if she scored at least twice the marks of Bob’s score. Determine whether she is happy or not.

# cook your dish here
x, y = map(int, input().split())

if x >= 2*y:
    print("Yes")
else:
    print("No")