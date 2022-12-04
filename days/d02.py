from day import Day

POINTS_FROM_SHAPE = {
    "X": 1, #rock
    "Y": 2, #paper
    "Z": 3  #scissors
}
GAME_COMBINATIONS = {
    "WIN":  ('A Y', 'B Z', 'C X'),
    "DRAW": ('A X', 'B Y', 'C Z'),
    "LOSE": ('A Z', 'B X', 'C Y')
}

class Day2(Day):
    def __init__(self) -> None:
        super().__init__(2, False)

    def _points_from_outcome_and_shape(self, game_outcome, oponents_shape):
        combinations = GAME_COMBINATIONS[game_outcome]
        combination = list(filter(lambda x: x.split(' ')[0] == oponents_shape, combinations))[0]
        shape = combination.split(' ')[1]
        points = POINTS_FROM_SHAPE[shape]
        return points

    def part1(self):
        predicted_score = 0
        for game in self.input_lines:
            my_shape = game.split(' ')[1]
            my_points = POINTS_FROM_SHAPE[my_shape]
            if game in GAME_COMBINATIONS['WIN']:
                game_outcome_score = 6
            elif game in GAME_COMBINATIONS['DRAW']:
                game_outcome_score = 3
            else:
                game_outcome_score = 0
            final_game_score = my_points + game_outcome_score
            predicted_score += final_game_score
        return predicted_score
    
    def part2(self):
        predicted_score = 0
        for game in self.input_lines:
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
            my_points = self._points_from_outcome_and_shape(game_outcome, oponents_shape)
            final_game_score = my_points + game_outcome_score
            predicted_score += final_game_score
        return predicted_score

if __name__ == '__main__':
    day2 = Day2()
    day2_part1_solution = day2.part1()
    day2_part2_solution = day2.part2()

    print(day2_part1_solution)
    print(day2_part2_solution)