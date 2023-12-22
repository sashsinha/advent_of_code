import utils


def part_1(data: str) -> int:
    pass


def part_2(data: str) -> int:
    pass


def main() -> None:
    data = utils.read_data_as_line('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2015)
    main()
