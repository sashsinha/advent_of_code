import utils


def part_1(data: str) -> str:
    program = list('abcdefghijklmnop')
    for move in data.split(','):
        if move.startswith('s'):
            x = int(move[1:])
            x = x % len(program)
            program = program[-x:] + program[:-x]
        elif move.startswith('x'):
            t = move[1:]
            a, b = map(int, t.split('/'))
            program[a], program[b] = program[b], program[a]
        elif move.startswith('p'):
            t = move[1:]
            p_a, p_b = t.split('/')
            a, b = program.index(p_a), program.index(p_b)
            program[a], program[b] = program[b], program[a]
    return ''.join(program)


def part_2(data: str) -> str:
    seen_programs = []
    program = list('abcdefghijklmnop')
    while ''.join(program) not in seen_programs:
        seen_programs.append(''.join(program))
        for move in data.split(','):
            if move.startswith('s'):
                x = int(move[1:])
                x = x % len(program)
                program = program[-x:] + program[:-x]
            elif move.startswith('x'):
                t = move[1:]
                a, b = map(int, t.split('/'))
                program[a], program[b] = program[b], program[a]
            elif move.startswith('p'):
                t = move[1:]
                p_a, p_b = t.split('/')
                a, b = program.index(p_a), program.index(p_b)
                program[a], program[b] = program[b], program[a]
    x = 1000000000 % len(seen_programs)
    return seen_programs[x]


def main() -> None:
    data = utils.read_data_as_line('day16.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=16, year=2017)
    main()
