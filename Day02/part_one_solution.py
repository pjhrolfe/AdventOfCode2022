ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

def calculate_score(move, outcome):
    score = 0

    if move == 0:
        score += ROCK_SCORE
    elif move == 1:
        score += PAPER_SCORE
    elif move == 2:
        score += SCISSORS_SCORE
    else:
        print("INVALID MOVE")

    if outcome == 0:
        score += DRAW_SCORE
    elif outcome == 1:
        score += LOSS_SCORE
    elif outcome == 2:
        score += WIN_SCORE
    else:
        print("INVALID OUTCOME")

    return score



def rock_paper_scissors(player_1_move, player_2_move):    
    if player_1_move == player_2_move:
        # 0 0
        # 1 1
        # 2 2
        return 0
    elif player_1_move == 0 and player_2_move == 1:
        # 0 1
        return 2
    elif player_1_move == 0 and player_2_move == 2:
        # 0 2
        return 1
    elif player_1_move == 1 and player_2_move == 0:
        # 1 0
        return 1
    elif player_1_move == 1 and player_2_move == 2:
        # 1 2
        return 2
    elif player_1_move == 2 and player_2_move == 0:
        # 2 0
        return 2
    elif player_1_move == 2 and player_2_move == 1:
        # 2 1
        return 1
    else:
        print("INVALID INPUT")

def main():
    total_player_2_score = 0

    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            split_line = line.split(" ")

            player_1_move = -1
            player_2_move = -1
            
            if split_line[0] == 'A':
                player_1_move = 0
            elif split_line[0] == 'B':
                player_1_move = 1
            elif split_line[0] == 'C':
                player_1_move = 2
            else:
                print("INVALID INPUT IN LEFT COLUMN")
            
            if split_line[1] == 'X':
                player_2_move = 0
            elif split_line[1] == 'Y':
                player_2_move = 1
            elif split_line[1] == 'Z':  
                player_2_move = 2
            else:
                print("INVALID INPUT IN RIGHT COLUMN")

            outcome = rock_paper_scissors(player_1_move, player_2_move)
            player_2_score = calculate_score(player_2_move, outcome)
            total_player_2_score += player_2_score

    print(total_player_2_score)

if __name__ == "__main__":
    main()