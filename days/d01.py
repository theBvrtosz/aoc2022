from day import Day

class Day1(Day):
    def __init__(self) -> None:
        super().__init__(1, False)
        self.get_kcal_per_elf()

    def get_kcal_per_elf(self):
        kcal_per_elf = []
        elf_kcal = 0
        for kcal in self.input_lines:
            if not kcal:
                kcal_per_elf.append(elf_kcal)
                elf_kcal = 0
                continue
            elf_kcal += int(kcal)
        kcal_per_elf.append(elf_kcal)
        self._kcal_per_elf = kcal_per_elf

    def part1(self):
        return max(self._kcal_per_elf)

    def part2(self):
        self._kcal_per_elf.sort(reverse=True)
        return sum(self._kcal_per_elf[:3])

if __name__ == '__main__':
    
    day1 = Day1()
    day1_part1_solution = day1.part1()
    day1_part2_solution = day1.part2()

    print(day1_part1_solution)
    print(day1_part2_solution)
