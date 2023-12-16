import utils


def part_1(data: list[str]) -> int:
    items = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')
    for i, line in enumerate(data, start=1):
        if sum(item in line for item in items) == 3:
            return i


def part_2(data: list[str]) -> int:
    items = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split('\n')
    items_dict = utils.read_lines_as_dict(items)
    for i, line in enumerate(data, start=1):
        sue, sue_items = line.split(':', maxsplit=1)
        count = 0
        for item in sue_items.split(','):
            key, value = item.split(':')
            key, value = key.strip(), int(value)
            found = False
            if key in {'cats', 'trees'}:
                found = value > items_dict[key]
            elif key in {'pomeranians', 'goldfish'}:
                found = value < items_dict[key]
            else:
                found = value == items_dict[key]
            if found:
                count += 1
        if count == 3:
            return i


def main() -> None:
    data = utils.read_data_as_lines('day16.txt')
    print(part_1(data))
    print(part_2(data))


if __name__ == '__main__':
    utils.download_data(day=16, year=2015)
    main()
