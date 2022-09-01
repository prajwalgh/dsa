a='''A. Parkway Walk
https://codeforces.com/contest/1697/problem/A
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are walking through a parkway near your house. The parkway has n+1 benches in a row numbered from 1 to n+1 from left to right. The distance between the bench i and i+1 is ai meters.

Initially, you have m units of energy. To walk 1 meter of distance, you spend 1 unit of your energy. You can't walk if you have no energy. Also, you can restore your energy by sitting on benches (and this is the only way to restore the energy). When you are sitting, you can restore any integer amount of energy you want (if you sit longer, you restore more energy). Note that the amount of your energy can exceed m.

Your task is to find the minimum amount of energy you have to restore (by sitting on benches) to reach the bench n+1 (and end your walk).

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤100) — the number of test cases. Then t test cases follow.

The first line of the test case contains two integers n and m (1≤n≤100; 1≤m≤104).

The second line of the test case contains n integers a1,a2,…,an (1≤ai≤100), where ai is the distance between benches i and i+1.

Output
For each test case, print one integer — the minimum amount of energy you have to restore (by sitting on benches) to reach the bench n+1 (and end your walk) in the corresponding test case.'''

t=int(input())
OUT=[]
while t>0:
    n,m=input().split()
    n=int(n)
    m=int(m)
    dist1=input().split()
    dist=[int(a) for a in dist1]
    output=0
    if sum(dist)<m:
        OUT.append(0)
        t-=1
        continue
    for a in dist:
        if m > a:
            m=m-a
            dist.pop(0)
    s=sum(dist)-m
    OUT.append(s)
    t-=1
    continue
for i in range(len(OUT)):
    print(OUT[i])

c='''C. awoo's Favorite Problem
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given two strings s and t, both of length n. Each character in both string is 'a', 'b' or 'c'.

In one move, you can perform one of the following actions:

choose an occurrence of "ab" in s and replace it with "ba";
choose an occurrence of "bc" in s and replace it with "cb".
You are allowed to perform an arbitrary amount of moves (possibly, zero). Can you change string s to make it equal to string t?

Input
The first line contains a single integer q (1≤q≤104) — the number of testcases.

The first line of each testcase contains a single integer n (1≤n≤105) — the length of strings s and t.

The second line contains string s of length n. Each character is 'a', 'b' or 'c'.

The third line contains string t of length n. Each character is 'a', 'b' or 'c'.

The sum of n over all testcases doesn't exceed 105.

Output
For each testcase, print "YES" if you can change string s to make it equal to string t by performing an arbitrary amount of moves (possibly, zero). Otherwise, print "NO".

Example
inputCopy
5
3
cab
cab
1
a
b
6
abbabc
bbaacb
10
bcaabababc
cbbababaac
2
ba
ab
outputCopy
YES
NO
YES
YES
NO
'''