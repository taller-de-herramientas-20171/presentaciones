#!/usr/bin/python3


def sum(M):
    acc = 0
    for i in range(1, M + 1):
        acc += 3 * i / (i**3 + 1)
    return acc


def testSum():
    epsilon = 0.1
    paso_todo = True
    paso_todo = paso_todo and (3.334 - sum(100)) < epsilon
    paso_todo = paso_todo and (3.334 - sum(1000)) < epsilon
    paso_todo = paso_todo and (3.334 - sum(100000)) < epsilon
    print(paso_todo)

testSum()
