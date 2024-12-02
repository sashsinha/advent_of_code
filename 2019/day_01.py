"""Advent of Code 2019, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2019.day_01
"""

import utils


def part_1(data: list[int]) -> int:
  total = 0
  for module in data:
    fuel = module // 3 - 2
    total += fuel
  return total


def part_2(data: list[int]) -> int:
  total = 0
  for module in data:
    fuel = module // 3 - 2
    while fuel > 0:
      total += fuel
      fuel = fuel // 3 - 2
  return total


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_int_lines('2019/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_int_lines('2019/day_01.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_int_lines('2019/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_int_lines('2019/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2019)
  utils.download_data(day=1, year=2019)
  main()
