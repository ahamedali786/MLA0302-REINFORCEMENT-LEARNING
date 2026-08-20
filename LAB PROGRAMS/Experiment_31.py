"""An autonomous robot navigates through a partially observable environment with limited
sensor information and uncertainty. Implement a partially observable Markov decision
process (POMDP) framework to enable the robot to localize itself and plan navigation
actions robustly under partial observability. Write a Python program to simulate the robot&#39;s
navigation process and evaluate its performance in different scenarios."""

import numpy as np

STATES = ["Left", "Center", "Right"]
ACTIONS = ["Left", "Right"]

def simulate():
    position = 1
    goal = 2
    steps = 0
    correct = 0

    print("\nStarting Robot Navigation...")
    
    for _ in range(10):
        # Limited sensor information
        sensor = np.random.choice(["Left", "Center", "Right"])

        # Belief-based decision
        if sensor == "Right":
            action = "Right"
        elif sensor == "Left":
            action = "Right"
        else:
            action = "Right"

        # Robot movement with uncertainty
        if action == "Right":
            if np.random.random() < 0.8:
                position = min(position + 1, 2)
            else:
                position = max(position - 1, 0)

        steps += 1

        if position == goal:
            correct += 1
            break

    return position, steps, correct


def evaluate():
    results = []

    for scenario in range(5):
        position, steps, success = simulate()

        if success:
            status = "Success"
        else:
            status = "Failure"

        results.append(success)

        print("Scenario", scenario + 1,
              "| Final Position:", STATES[position],
              "| Steps:", steps,
              "| Status:", status)

    success_rate = np.mean(results) * 100

    print("\nPerformance Evaluation:")
    print("Successful Scenarios:", sum(results))
    print("Total Scenarios:", len(results))
    print("Success Rate:", round(success_rate, 2), "%")


def main():
    position, steps, success = simulate()

    print("\nOutput:")
    print("Robot Final Position:", STATES[position])
    print("Steps Taken:", steps)

    if success:
        print("Navigation Status: Goal Reached")
    else:
        print("Navigation Status: Goal Not Reached")


while True:
    print("\n====== POMDP Robot Navigation ======")
    print("1. Simulate Robot Navigation")
    print("2. Evaluate Different Scenarios")
    print("3. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        main()

    elif ch == "2":
        evaluate()

    elif ch == "3":
        print("\nProgram Ended")
        break

    else:
        print("Invalid Choice")

OUTPUT :
====== POMDP Robot Navigation ======
1. Simulate Robot Navigation
2. Evaluate Different Scenarios
3. Exit
Enter Choice: 1

Starting Robot Navigation...

Output:
Robot Final Position: Right
Steps Taken: 9
Navigation Status: Goal Reached

====== POMDP Robot Navigation ======
1. Simulate Robot Navigation
2. Evaluate Different Scenarios
3. Exit
Enter Choice: 2

Starting Robot Navigation...
Scenario 1 | Final Position: Right | Steps: 1 | Status: Success

Starting Robot Navigation...
Scenario 2 | Final Position: Right | Steps: 1 | Status: Success

Starting Robot Navigation...
Scenario 3 | Final Position: Right | Steps: 4 | Status: Success

Starting Robot Navigation...
Scenario 4 | Final Position: Right | Steps: 1 | Status: Success

Starting Robot Navigation...
Scenario 5 | Final Position: Right | Steps: 1 | Status: Success

Performance Evaluation:
Successful Scenarios: 5
Total Scenarios: 5
Success Rate: 100.0 %

====== POMDP Robot Navigation ======
1. Simulate Robot Navigation
2. Evaluate Different Scenarios
3. Exit
Enter Choice: 3

Program Ended
