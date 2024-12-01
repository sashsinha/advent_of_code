"""Advent of Code 2023, Day 1 Solution.

Usage:
  (advent_of_code) $ uv run -m 2023.day_01
"""

import utils

_DIGIT_BY_NAME = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
}


def part_1(data: list[str]) -> int:
  total = 0
  for line in data:
    digits = [c for c in line if c.isdigit()]
    first, last = digits[0], digits[-1]
    total += int(f'{first}{last}')
  return total


def part_2(data: str) -> int:
  total = 0
  for line in data:
    first_digit = None
    first_index = len(line)
    last_digit = None
    last_index = -1
    for word, digit in _DIGIT_BY_NAME.items():
      index = line.find(word)
      if index != -1 and index < first_index:
        first_digit = digit
        first_index = index
      index = line.rfind(word)
      if index != -1 and index > last_index:
        last_digit = digit
        last_index = index
    for i, char in enumerate(line):
      if char.isdigit():
        if i < first_index:
          first_digit = int(char)
          first_index = i
        if i > last_index:
          last_digit = int(char)
          last_index = i
    total += int(f'{first_digit}{last_digit}')
  return total


def main() -> None:
  data = utils.read_data_as_lines('2023/day_01.txt')
  print(part_1(data))
  print(part_2(data))


if __name__ == '__main__':
  utils.download_data(day=1, year=2023)
  main()
