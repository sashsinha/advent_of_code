"""Advent of Code 2020, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2020.day_01
"""

import utils


def part_1(data: list[int]) -> int:
  for x in data[:-1]:
    for y in data[1:]:
      if x + y == 2020:
        return x * y


def part_2(data: list[int]) -> int:
  for x in data[:-2]:
    for y in data[1:-1]:
      for z in data[2:-2]:
        if x + y + z == 2020:
          return x * y * z


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_int_lines('2020/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_int_lines('2020/day_01.txt')
  print(f'Part 2 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_int_lines('2020/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_int_lines('2020/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2020)
  utils.download_data(day=1, year=2020)
  main()
