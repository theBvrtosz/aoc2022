from day import Day 

class Day6(Day):
    def __init__(self) -> None:
        super().__init__(6, False)

    def part1(self):
        letters_till_marker = 0
        buffer = self.input_lines[0]
        marker = []
        for letter in buffer:
            letters_till_marker += 1
            marker.append(letter)
            marker_len = len(marker)
            # removing first marker char to retain len(marker) == 4
            if marker_len > 4:
                marker = marker[1:]
            unique_marker_letters_count = len(set(marker))
            if unique_marker_letters_count == 4:
                break
        return letters_till_marker

    def part2(self):
        letters_till_marker = 0
        buffer = self.input_lines[0]
        marker = []
        for letter in buffer:
            letters_till_marker += 1
            marker.append(letter)
            marker_len = len(marker)
            # removing first marker char to retain len(marker) == 4
            if marker_len > 14:
                marker = marker[1:]
            unique_marker_letters_count = len(set(marker))
            if unique_marker_letters_count == 14:
                break
        return letters_till_marker

if __name__ == '__main__':
    day6 = Day6()
    day6_part1_solution = day6.part1()
    print(day6_part1_solution)
    day6_part2_solution = day6.part2()
    print(day6_part2_solution)