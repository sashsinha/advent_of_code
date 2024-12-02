"""Advent of Code 2021, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2021.day_01
"""

from more_itertools import windowed

import utils


def part_1(data: list[int]) -> int:
  increases = 0
  for a, b in zip(data[:-1], data[1:]):
    if b > a:
      increases += 1
  return increases


def part_2(data: list[int]) -> int:
  increases = 0
  prev = None
  for window in windowed(data, n=3):
    if prev and sum(window) > prev:
      increases += 1
    prev = sum(window)
  return increases


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_int_lines('2021/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_int_lines('2021/day_01.txt')
  print(f'Part 2 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_int_lines('2021/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_int_lines('2021/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2021)
  utils.download_data(day=1, year=2021)
  main()
