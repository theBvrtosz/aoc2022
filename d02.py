points_from_shape = {
    "X": 1, #rock
    "Y": 2, #paper
    "Z": 3  #scissors
}
game_combinations = {
    "WIN":  ('A Y', 'B Z', 'C X'),
    "DRAW": ('A X', 'B Y', 'C Z'),
    "LOSE": ('A Z', 'B X', 'C Y')
}

def d02_p1(input):
    games = input.splitlines()
    predicted_score = 0
    for game in games:
        my_shape = game.split(' ')[1]
        my_points = points_from_shape[my_shape]
        if game in game_combinations['WIN']:
            game_outcome_score = 6
        elif game in game_combinations['DRAW']:
            game_outcome_score = 3
        else:
            game_outcome_score = 0
        final_game_score = my_points + game_outcome_score
        predicted_score += final_game_score
    return predicted_score


def points_from_outcome_and_shape(game_outcome, oponents_shape):
    combinations = game_combinations[game_outcome]
    combination = list(filter(lambda x: x.split(' ')[0] == oponents_shape, combinations))[0]
    shape = combination.split(' ')[1]
    points = points_from_shape[shape]
    return points

def d02_p2(input):
    games = input.splitlines()
    predicted_score = 0
    for game in games:
        oponents_shape, suggested_game_outcome = game.split(' ')
        if suggested_game_outcome == 'X': # LOSE
            game_outcome = 'LOSE'
            game_outcome_score = 0
        elif suggested_game_outcome == 'Y': # DRAW
            game_outcome = 'DRAW'
            game_outcome_score = 3
        else: # WIN
            game_outcome = 'WIN'
            game_outcome_score = 6
        my_points = points_from_outcome_and_shape(game_outcome, oponents_shape)
        final_game_score = my_points + game_outcome_score
        predicted_score += final_game_score
    return predicted_score

if __name__ == '__main__':
    with open('inputs/d02-input.txt', 'r') as f:
        cnt = f.read()
    d02_p01_answ = d02_p1(cnt)
    print(d02_p01_answ)
    d02_p02_answ = d02_p2(cnt)
    print(d02_p02_answ)