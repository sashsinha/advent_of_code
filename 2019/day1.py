import utils


def get_fuel(mass: int) -> int:
    return mass // 3 - 2


def get_fuel2(mass: int) -> int:
    total_fuel = 0
    fuel = get_fuel(mass)
    total_fuel += fuel
    while fuel > 6:
        fuel = get_fuel(fuel)
        total_fuel += fuel
    return total_fuel


def part_1(data: list[str]) -> int:
    return sum(map(get_fuel, map(int, data)))


def part_2(data: list[str]) -> int:
    return sum(map(get_fuel2, map(int, data)))


def main() -> None:
    data = utils.read_data_as_lines('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2019)
    main()
