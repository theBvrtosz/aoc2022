from day import Day

class Day5(Day):
    def __init__(self) -> None:
        super().__init__(5, False)
        self._get_crates()
        self._get_instructions()

    def part1(self):
        print(self._crates)
        for instruction in self._instructions:
            instuctions_arr = instruction.split(' ')
            move, source, target = map(int, (instuctions_arr[1], instuctions_arr[3], instuctions_arr[5]))

            source_stack = self._crates[source - 1]
            source_stack_len = len(source_stack)
            crates_to_move = source_stack[source_stack_len - move:][::-1]
            # move crates to target
            self._crates[target - 1].extend(crates_to_move)
            # remove crates from source
            self._crates[source - 1] = source_stack[:source_stack_len - move]
        
        last_crates = ''
        for crate in self._crates:
            last_crates += crate[-1]
        return last_crates
    
    def part2(self):
        print(self._crates)
        for instruction in self._instructions:
            instuctions_arr = instruction.split(' ')
            move, source, target = map(int, (instuctions_arr[1], instuctions_arr[3], instuctions_arr[5]))

            source_stack = self._crates[source - 1]
            source_stack_len = len(source_stack)
            crates_to_move = source_stack[source_stack_len - move:]
            # move crates to target
            self._crates[target - 1].extend(crates_to_move)
            # remove crates from source
            self._crates[source - 1] = source_stack[:source_stack_len - move]
        
        last_crates = ''
        for crate in self._crates:
            last_crates += crate[-1]
        return last_crates
    
    def _get_crates(self):
        sep = self.input_lines.index('')
        crates = self.input_lines[:sep]
        no_of_stacks = len(crates[-1].replace(' ', ''))
        crates_transposed = [[] for _ in range(no_of_stacks)]

        for crate_line in crates[:-1][::-1]:
            line_no_whitespace = crate_line.replace('    ', ' [] ').split(' ')
            line_no_whitespace_list = list(filter(lambda x: x != '', line_no_whitespace))

            for i in range(len(line_no_whitespace_list)):
                crate = line_no_whitespace_list[i]
                if crate != '[]':
                    crates_transposed[i].append(crate[1])
        self._crates = crates_transposed

    def _get_instructions(self):
        sep = self.input_lines.index('')
        self._instructions = self.input_lines[sep+1:]


        
if __name__ == '__main__':
    day5 = Day5()
    day5_part1_solution = day5.part2()
    print(day5_part1_solution)
    