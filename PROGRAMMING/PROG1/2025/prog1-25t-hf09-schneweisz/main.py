import os
from play import load_play, get_speech_count

def main():
    """The Main Menu of the program."""
    play = None
    play_name = None

    while True:
        print(f"\nCurrently opened play: {play_name if play_name else 'None'}")
        print(f"Total number of speeches: {get_speech_count(play) if play else 0}")
        print(
            """ 

Main menu:
1: Open a play from a directory
2: List scenes of a character
3: Display number of speeches by characters
0: Exit"""
        )
        choice = input("Select a menu option: ")
        if choice == "1":
            directory = input("Enter the path to the play directory: ")
            if os.path.exists(directory):
                try:
                    play = load_play(directory)
                    play_name = os.path.basename(directory)
                except FileNotFoundError:
                    print("Error: Directory not found.")
            else:
                print("Error: Invalid directory.")
        elif choice == "2":
            if not play:
                print("Error: No play loaded.")
                continue
            character = input("Enter character name: ").upper()
            scenes = [scene for scene, characters in play.items() if character in characters]
            if scenes:
                print("\n".join(scenes))
            else:
                print("Error: No character with this name.")
        elif choice == "3":
            if not play:
                print("Error: No play loaded.")
                continue
            from collections import Counter
            import matplotlib.pyplot as plt

            
            speech_counts = Counter(character for characters in play.values() for character in characters)

            # Horizontal bar chart
            plt.figure(figsize=(10, 6))
            plt.barh(list(speech_counts.keys()), list(speech_counts.values()))
            plt.title(f"Speech Count by Characters in {play_name}")
            plt.xlabel("Number of Speeches")
            plt.ylabel("Characters")
            plt.show()

            # Pie chart
            plt.figure(figsize=(8, 8))
            plt.pie(speech_counts.values(), labels=speech_counts.keys(), autopct='%1.1f%%')
            plt.title(f"Speech Distribution in {play_name}")
            plt.show()

            for character, count in speech_counts.items():
                print(f"{character}: {count}")
        elif choice == "0":
            break
        else:
            print("Error: Invalid option.")


if __name__ == "__main__":
    main()