import utils


def part_1(data: str) -> int:
    floor = 0
    for ch in data:
        if ch == ')':
            floor -= 1
        elif ch == '(':
            floor += 1
    return floor


def part_2(data: str) -> int:
    floor = 0
    for i, ch in enumerate(data, start=1):
        if ch == ')':
            floor -= 1
        elif ch == '(':
            floor += 1
        if floor == -1:
            return i
    return -1


def main() -> None:
    data = utils.read_data_as_line('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2015)
    main()
