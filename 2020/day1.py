import utils


def part_1(data: list[str]) -> int:
    data = list(map(int, data))
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            if i == j:
                continue
            if x + y == 2020:
                return x * y


def part_2(data: list[str]) -> int:
    data = list(map(int, data))
    for i, x in enumerate(data):
        for j, y in enumerate(data):
            for k, z in enumerate(data):
                if i == j or i == z or j == k:
                    continue
                if x + y + z == 2020:
                    return x * y * z


def main() -> None:
    data = utils.read_data_as_lines('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2020)
    main()
