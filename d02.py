points_from_shape = {
    "A": 1, #rock
    "B": 2, #paper
    "C": 3, #scissors
    "X": 1, #rock
    "Y": 2, #paper
    "Z": 3  #scissors
}

def d02_p1(input):
    games = input.splitlines()
    predicted_score = 0
    for game in games:
        oponents_shape, my_shape = game.split(' ')
        oponents_points = points_from_shape[oponents_shape]
        my_points = points_from_shape[my_shape]
        
        if my_points > oponents_points:
            game_outcome_points = 6
        elif my_points == oponents_points:
            game_outcome_points = 3
        else:
            game_outcome_points = 0
        game_score = game_outcome_points + my_points
        print(game)
        print(oponents_points, my_points)
        print(game_outcome_points)
        print(game_score)
        
        predicted_score += game_score
        print(predicted_score)
    return predicted_score


if __name__ == '__main__':
    with open('inputs/d02-input-kartezjan.txt', 'r') as f:
        cnt = f.read()
    d02_p01_answ = d02_p1(cnt)
    print(d02_p01_answ)