def get_kcal_per_elf(input):
    kcal_per_elf = []
    elf_kcal = 0
    for kcal in input.splitlines():
        if not kcal:
            kcal_per_elf.append(elf_kcal)
            elf_kcal = 0
            continue
        elf_kcal += int(kcal)
    kcal_per_elf.append(elf_kcal)
    return kcal_per_elf


if __name__ == '__main__':
    with open('inputs/d01-input.txt', 'r') as f:
        cnt = f.read()
    kcal_per_elf = get_kcal_per_elf(cnt)
    print(max(kcal_per_elf))    #part1

    kcal_per_elf.sort(reverse=True)
    print(sum(kcal_per_elf[:3])) #part2
