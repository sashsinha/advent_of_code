import collections
import utils


def part_1(data: str) -> int:
    presents = collections.defaultdict(int)
    presents[(0, 0)] += 1
    x, y = 0, 0
    for move in data:
        if move == '<':
            x -= 1
        elif move == '>':
            x += 1
        elif move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        presents[(x, y)] += 1
    return len(presents)


def part_2(data: str) -> int:
    presents = collections.defaultdict(int)
    presents[(0, 0)] += 2
    x, y = 0, 0
    r_x, r_y = 0, 0
    for i, move in enumerate(data):
        if i % 2 == 0:
            if move == '<':
                x -= 1
            elif move == '>':
                x += 1
            elif move == '^':
                y += 1
            elif move == 'v':
                y -= 1
            presents[(x, y)] += 1
        else:
            if move == '<':
                r_x -= 1
            elif move == '>':
                r_x += 1
            elif move == '^':
                r_y += 1
            elif move == 'v':
                r_y -= 1
            presents[(r_x, r_y)] += 1
    return len(presents)


def main() -> None:
    data = utils.read_data_as_line('day3.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=3, year=2015)
    main()
