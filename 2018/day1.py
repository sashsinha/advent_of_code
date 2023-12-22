import itertools
import utils


def part_1(data: list[str]) -> int:
    frequency = 0
    for change in data:
        is_negative, value = change[0] == '-', int(change[1:])
        frequency += value if not is_negative else -1 * value
    return frequency


def part_2(data: list[str]) -> int:
    frequency = 0
    seen_frequencies = {frequency}
    for change in itertools.cycle(data):
        is_negative, value = change[0] == '-', int(change[1:])
        frequency += value if not is_negative else -1 * value
        if frequency in seen_frequencies:
            return frequency
        seen_frequencies.add(frequency)
    return -1


def main() -> None:
    data = utils.read_data_as_lines('day1.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=1, year=2018)
    main()
