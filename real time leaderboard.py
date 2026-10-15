
import time

# Store player scores
players = {}

def add_player():
    name = input("Enter player name: ")
    if name not in players:
        players[name] = 0
        print(name, "added successfully!")
    else:
        print("Player already exists!")

def update_score():
    name = input("Enter player name: ")

    if name in players:
        score = int(input("Enter points to add: "))
        players[name] += score
        print("Score updated successfully!")
    else:
        print("Player not found!")

def show_leaderboard():
    print("\n===== REAL-TIME LEADERBOARD =====")

    if not players:
        print("No players available.")
        return

    sorted_players = sorted(
        players.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("Rank   Player          Score")
    print("-" * 32)

    for rank, (name, score) in enumerate(sorted_players, start=1):
        print(f"{rank:<6} {name:<15} {score}")

def main():
    while True:
        print("\n1. Add Player")
        print("2. Update Score")
        print("3. Show Leaderboard")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            update_score()
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            print("Leaderboard closed.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
