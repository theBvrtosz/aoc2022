def get_kcal_per_elve(input):
    kcal_per_elve = []
    elve_kcal = 0
    for kcal in input.split('\n'):
        if kcal == '':
            kcal_per_elve.append(elve_kcal)
            elve_kcal = 0
            continue
        elve_kcal += int(kcal)
    kcal_per_elve.sort(reverse=True)
    return kcal_per_elve


if __name__ == '__main__':
    with open('inputs/d01-input.txt', 'r') as f:
        cnt = f.read()
    kcal_per_elve = get_kcal_per_elve(cnt)
    #part1
    print(kcal_per_elve[0])
    #part2
    print(sum(kcal_per_elve[:3]))