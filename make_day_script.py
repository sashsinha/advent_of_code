"""Generates Python files for solving a day of Advent of Code.

Example usage:
  uv run make_day_script.py 1 2024
"""

import argparse
import os
import textwrap

_TRIPLE_QUOTES = '"""'


def _get_day_script_docstring(day: int, year: int) -> str:
  return f"""\
{_TRIPLE_QUOTES}Advent of Code {year}, Day {day} Solution.

Usage:
  (advent_of_code) $ uv run -m {year}.day_{day:0>2}
{_TRIPLE_QUOTES}"""


def main() -> None:
  parser = argparse.ArgumentParser(
    description='Generate Advent of Code day script.'
  )
  parser.add_argument(
    'day', type=int, help='The day of the Advent of Code problem.'
  )
  parser.add_argument(
    'year', type=int, help='The year of the Advent of Code problem.'
  )
  args = parser.parse_args()
  day = args.day
  year = args.year
  day_script = textwrap.dedent(f"""\
{_get_day_script_docstring(day, year)}

import utils


def part_1(data: str) -> int:
  pass


def part_2(data: str) -> int:
  pass


def main() -> None:
  data = utils.read_data_as_line('{year}/day_{day:0>2}.txt')
  print(part_1(data))
  print(part_2(data))


if __name__ == '__main__':
  utils.download_data(day={day}, year={year})
  main()
""")
  if not os.path.exists(str(year)):
    os.makedirs(str(year))
  file_path = f'{year}/day_{day:0>2}.py'
  if os.path.exists(file_path):
    print(f"Error: File '{file_path}' already exists.")
  else:
    with open(file_path, 'w') as f:
      f.write(day_script)


if __name__ == '__main__':
  main()
