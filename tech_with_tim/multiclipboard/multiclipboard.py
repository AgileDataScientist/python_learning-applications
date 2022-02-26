# YouTube: Tech With Tim - 3 Automation Projects for Beginners (https://youtu.be/Oz3W-LKfafE)

# Import Python standard modules
import sys
import json
#import clipboard
import pyperclip as pc


# Save key and value to the JSON data file
SAVED_DATA = "clipboard.json"


# Write to data file
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# Read from a data file
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    # Prints the arguments submitted with command
    print(sys.argv)

    # Get the single command
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    # Enter one of three commands: save, list, and load
    if command.lower() == "save":
        key = input("Please enter a key: ")
        data[key] = pc.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command.lower() == "load":
        key = input("Please enter a key: ")
        if key in data:
            pc.copy(data[key])
            print("Data copied from clipboard!")
        else:
            print("Key does not exist!")
    elif command.lower() == "list":
        print(data)
    else:
        print("Unknown command.")

else:

    # Prints the arguments submitted with command
    print(sys.argv)

    print("Please pass exactly one command.")
