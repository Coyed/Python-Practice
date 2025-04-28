import random
import time

def display_race(player_position, computer_position):
    print("Player: " + "-" * player_position + "P")
    print("Computer: " + "-" * computer_position + "C")

def race():
    track_lengths = [30, 40, 50]  # Different track lengths
    track_difficulty = [1, 2, 3]  # Corresponding difficulty levels

    print("Choose a track:")
    for i, length in enumerate(track_lengths, start=1):
        print(f"{i}. Track length: {length}")

    track_choice = int(input("Enter track number: ")) - 1
    if track_choice < 0 or track_choice >= len(track_lengths):
        print("Invalid track choice. dipshit")
        return

    track_length = track_lengths[track_choice]
    difficulty = track_difficulty[track_choice]

    player_position = 0
    computer_position = 0

    print(f"Get ready for a race on a track of length {track_length}!")
    time.sleep(1)

    while player_position < track_length and computer_position < track_length:
        display_race(player_position, computer_position)

        input("Click anywhere to accelerate...")
        player_position += random.randint(1, 3) * difficulty

        computer_position += random.randint(1, 3) * difficulty

        print("\033c", end="")
        time.sleep(0.5)

    display_race(player_position, computer_position)

    if player_position >= track_length:
        print("You won! f*ck that dumb*ss bot! humans on top!")
    else:
        print("Computer won. you shithead, you suck, go pick up ur mom form the airport, you pr**k")

# Start the race
race()
