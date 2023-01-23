def main():
    calories_totals = []

    with open('input.txt') as f:
        lines = f.readlines()

        current_calories_seen = 0

        for line in lines:
            if (line == '\n'):
                calories_totals.append(current_calories_seen)
                current_calories_seen = 0
            else:
                current_calories_seen += int(line)

    calories_totals.sort(reverse=True)
    print(str(calories_totals[0] + calories_totals[1] + calories_totals[2]))
    pass

if __name__ == "__main__":
    main()