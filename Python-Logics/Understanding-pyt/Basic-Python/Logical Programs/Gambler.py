import random
def gamble(stake, goal, trials):
    wins = 0
    for i in range(trials):
        cash = stake
        while cash>0 and cash<goal:
            
            if random.random() < 0.5:
                cash += 1
            else:
                cash -= 1
        if cash==goal:
            wins += 1

    print(f"{wins} wins out of {trials} trials")
    print(f"Percent of games won = {100.0 * wins / trials:.2f}%")
    print(f"percent of games lost = {100.0 * (trials - wins) / trials:.2f}%")

stake = int(input("Enter the stake: "))
goal = int(input("Enter the goal: "))
trials = int(input("Enter the number of trials: "))
gamble(stake, goal, trials)