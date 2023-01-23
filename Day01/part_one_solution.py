def main():
    highest_calories_seen = 0

    with open('input.txt') as f:
        lines = f.readlines()

        current_calories_seen = 0

        for line in lines:
            if (line == '\n'):
                if highest_calories_seen < current_calories_seen:
                    highest_calories_seen = current_calories_seen
       
                current_calories_seen = 0
            else:
                current_calories_seen += int(line)

        print(highest_calories_seen)

    pass

if __name__ == "__main__":
    main()