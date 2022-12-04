from day import Day

class Day3(Day):
    def __init__(self) -> None:
        super().__init__(3, False)

    def part1(self):
        priorities_sum = 0
        for rucksack in self.input_lines:
            half_rucksack_pos = len(rucksack) // 2
            compartment1 = set(rucksack[:half_rucksack_pos])
            compartment2 = set(rucksack[half_rucksack_pos:])
            common_item = (compartment1&compartment2).pop()
            priority = self._get_item_priority(common_item)
            priorities_sum += priority
        return priorities_sum
            
    def part2(self):
        priorities_sum = 0
        for i in range(0, len(self.input_lines), 3):
            group = self.input_lines[i:i+3]
            rucksack1, rucksack2, rucksack3 = map(set, group)
            common_item = (rucksack1&rucksack2&rucksack3).pop()
            priority = self._get_item_priority(common_item)
            priorities_sum += priority
        return priorities_sum
    
    def _get_item_priority(self, item):
        if item.isupper():
            return ord(item) - ord('A') + 27
        else:
            return ord(item) - ord('a') + 1
    
if __name__ == '__main__':
    day3 = Day3()
    day3_part1_solution = day3.part1()
    day3_part2_solution = day3.part2()
    print(day3_part1_solution)
    print(day3_part2_solution)