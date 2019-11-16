'''
Created By: Anirudha Korde
Date: 16/11/2019
Modified By:

Description:
There are N people in village, who wants to visit Temple outside the village.
To reach the temple, villagers need to cross the river.
So, they hire the only available boat which can carry at most two people.
Villagers decided to hire this boat to reach safely by sailing it by themselves.
Every part of journey from village to temple and temple to village has some
cost associated with it which is given by an array A[] elements. Array A[] has n elements,
where A(i) represents the cost ith person has to pay if they sail the boat alone.
If two people sail the vehicle, the cost of travel will be the maximum of cost of two people.
Calculate the minimum total cost so that all N people can reach Temple safely.
'''

# Warnings
NLESSER = "Invalid Input:\n-> Hey there!!! Number of people cannot be less than one"
NGREATER = "Invalid Input:\n-> Hey there!!! there are no {} people in village"
TLESSER = "Invalid Input: \n-> Hey there!!! There are no test cases less than one"
TGREATER = "Invalid Input: \n-> Hey there!!! There are no {} test cases"
# End of Warnings

# Test cases
T1 = "Pair of first two people in the array have been selected and sent to the temple"
T2 = "Each pair shall go in a separate boat"
T3 = "Boat will contain the two people one with Max amount an one with Min amount of all the people"
# End of test cases
t = 0
n = 0
print("\n***************** Minimum Travelling fare **********************\n")


'''This while loop is used for selecting the particular Testcase'''
while t == 0 or t > 3:
    print("Following are the Test Cases : ")
    print("1. {}\n2. {}\n3. {}".format(T1,T2,T3))
    t = int(input("Enter the Test case number -->> "))
    if t < 1:
        print(TLESSER)
    if t > 3:
        print(TGREATER)

'''End of while loop for selecting the test case'''


'''This while loop is used for accepting the input for No. of people travelling'''
while n == 0 or n > 100000:
    n = int(input("Enter the no. of travelling people -->> "))
    if n < 1:
        print(NLESSER)
    elif n > 100000:
        print(NGREATER.format(n))
'''End of while loop for accepting the input'''


'''This while loop is used for accepting the cost for a particular person'''
cost = []
while len(cost) < n:
    temp = input("The cost for person {} -->> ".format(len(cost)+1))
    cost.append(temp)
'''End of while loop for accepting the cost'''


source_cost = cost  # Copying the cost to a temp list
dest_cost = []
total_cost = 0


if t == 1:
    print("\nYou have selected Test case 1:\n{}".format(T1))
    while len(source_cost) != 0 and len(dest_cost) != len(cost):
        boat = source_cost[:2]
        source_cost = source_cost[-(len(source_cost)-2):]
        total_cost = total_cost + int(max(boat))    # Travelling to temple cost

        if source_cost == boat:
            break;

        dest_cost.extend(boat)
        total_cost = total_cost + int(min(dest_cost))   # Travelling back from temple cost

        boat = min(dest_cost)
        dest_cost.remove(min(dest_cost))

        source_cost.append(boat)
    print("\nTotal Cost: {}".format(total_cost))

elif t == 2:
    print("\nYou have selected Test case 2:\n{}".format(T2))

    while len(source_cost) != 0 and len(dest_cost) != len(cost):
        boat = max(source_cost)
        source_cost = source_cost[-(len(source_cost)-2):]
        total_cost = total_cost + int(max(boat))

        if source_cost == boat:
            break;
    print("\nTotal Cost: {}".format(total_cost))


elif t == 3:
    print("\nYou have selected Test case 3:\n{}".format(T3))

    while len(source_cost) != 0 or len(dest_cost) != len(cost):
        boat = []
        boat.append(min(source_cost))
        boat.append(max(source_cost))
        source_cost.remove(min(source_cost))
        source_cost.remove(max(source_cost))
        total_cost = total_cost + int(max(boat))    # Travelling to temple cost
        if len(source_cost) == 0:
            break;

        dest_cost.extend(boat)
        total_cost = total_cost + int(min(dest_cost))   # Travelling from temple cost

        boat = min(dest_cost)

        dest_cost.remove(min(dest_cost))

        source_cost.append(boat)
    print("Total Cost: {}".format(total_cost))
