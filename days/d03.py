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
            common_item = list(compartment1&compartment2)[0]
            priority_change = 38 if common_item.isupper() else 96
            priority = ord(common_item) - priority_change
            priorities_sum += priority
        return priorities_sum
            
    def part2(self):
        priorities_sum = 0
        for i in range(0, len(self.input_lines), 3):
            group = self.input_lines[i:i+3]
            rucksack1 = set(group[0])
            rucksack2 = set(group[1])
            rucksack3 = set(group[2])
            common_item = list(rucksack1&rucksack2&rucksack3)[0]
            priority_change = 38 if common_item.isupper() else 96
            priority = ord(common_item) - priority_change
            priorities_sum += priority
        return priorities_sum
    
if __name__ == '__main__':
    day3 = Day3()
    day3_part1_solution = day3.part1()
    day3_part2_solution = day3.part2()
    print(day3_part1_solution)
    print(day3_part2_solution)