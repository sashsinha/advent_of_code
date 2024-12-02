"""Advent of Code 2018, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2018.day_01
"""

from itertools import cycle

import utils


def part_1(data: list[str]) -> int:
  frequency = 0
  for line in data:
    if line.startswith('+'):
      frequency += int(line[1:])
    elif line.startswith('-'):
      frequency -= int(line[1:])
  return frequency


def part_2(data: list[str]) -> int:
  seen_frequencies = {0}
  frequency = 0
  for line in cycle(data):
    if line.startswith('+'):
      frequency += int(line[1:])
    elif line.startswith('-'):
      frequency -= int(line[1:])
    if frequency in seen_frequencies:
      return frequency
    seen_frequencies.add(frequency)


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_lines('2018/day_01_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_lines('2018/day_01.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # # Part 2
  example_2_data = utils.read_data_as_lines('2018/day_01_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_lines('2018/day_01.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=1, year=2018)
  utils.download_data(day=1, year=2018)
  main()
