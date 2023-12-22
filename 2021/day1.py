import utils


def part_1(data: list[int]) -> int:
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def part_2(data: list[int]) -> int:
    return sum(sum(data[i:i + 3]) < sum(data[i + 1:i + 4]) for i in range(len(data) - 3))


def main() -> None:
    data = utils.read_data_as_int_lines('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2021)
    main()
