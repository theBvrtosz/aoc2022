from day import Day

class Day4(Day):
    def __init__(self) -> None:
        super().__init__(4, False)

    def part1(self):
        fully_contained_sections = 0
        for pair in self.input_lines:
            section1, section2 = pair.split(',')
            section1_start, section1_end = map(int, section1.split('-'))
            section2_start, section2_end = map(int, section2.split('-'))
            if section1_start <= section2_start and section1_end >= section2_end:
                # section 1 fully contains section 2
                fully_contained_sections += 1
            elif section2_start <= section1_start and section2_end >= section1_end:
                # section 2 fully contains section 1
                fully_contained_sections += 1
        return fully_contained_sections


if __name__ == '__main__':
    day4 = Day4() 
    day4_part1_solution = day4.part1()
    print(day4_part1_solution)
    
