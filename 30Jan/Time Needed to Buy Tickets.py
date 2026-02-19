from collections import deque


def timeRequiredToBuy(tickets, k):
    i = 0
    seconds = 0
    while(tickets[k]!=0):
        print("TIckets:", tickets)
        if(tickets[i]!=0):
            tickets[i] = tickets[i] - 1
            seconds+=1
        i+=1
        if(i==len(tickets)):
            i = 0

    return seconds

tickets = [2,5,2]
k = 2
print("Time taken by Kth person to buy all required tickets: ",timeRequiredToBuy(tickets, k))