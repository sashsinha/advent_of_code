"""Advent of Code 2024, Day 3 Solution.

Usage:
  (advent_of_code) $ uv run -m 2024.day_03
"""

import re

import utils


def part_1(data: str) -> int:
  total = 0
  pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
  matches = re.findall(pattern, data)
  for match in matches:
    num1 = int(match[0])
    num2 = int(match[1])
    total += num1 * num2
  return total


def part_2(data: str) -> int:
  total = 0
  enabled = True
  pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
  matches = re.findall(pattern, data)
  for match in matches:
    # print(match)
    if match[0] == 'do()':
      enabled = True
    elif match[0] == "don't()":
      enabled = False
    elif enabled:
      num1 = int(match[1])
      num2 = int(match[2])
      total += num1 * num2
  return total


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_line('2024/day_03_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_line('2024/day_03.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_line('2024/day_03_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_line('2024/day_03.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=3, year=2024)
  utils.download_data(day=3, year=2024)
  main()
