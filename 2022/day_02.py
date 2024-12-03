"""Advent of Code 2022, Day 2 Solution.

Usage:
  (advent_of_code) $ uv run -m 2022.day_02
"""

import utils

_MOVE_BY_LETTER = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors',
  'X': 'Rock',
  'Y': 'Paper',
  'Z': 'Scissors',
}

_SCORE_BY_MOVE = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3,
}

_MOVE_BY_LETTER2 = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors',
}

_OUTCOME_BY_LETTER = {
  'X': 'Loss',
  'Y': 'Draw',
  'Z': 'Win',
}


def part_1(data: list[str]) -> int:
  total_score = 0
  for round in data:
    a, b = round.split(' ')
    a_move, b_move = _MOVE_BY_LETTER[a], _MOVE_BY_LETTER[b]
    shape_score = _SCORE_BY_MOVE[b_move]
    outcome_score = 0
    if a_move != b_move:
      if a_move == 'Rock':
        if b_move == 'Paper':
          outcome_score = 6
      elif a_move == 'Paper':
        if b_move == 'Scissors':
          outcome_score = 6
      elif a_move == 'Scissors':
        if b_move == 'Rock':
          outcome_score = 6
    else:
      outcome_score = 3
    round_score = shape_score + outcome_score
    total_score += round_score
  return total_score


def part_2(data: list[str]) -> int:
  total_score = 0
  for round in data:
    a, b = round.split(' ')
    a_move = _MOVE_BY_LETTER2[a]
    b_outcome = _OUTCOME_BY_LETTER[b]
    if b_outcome == 'Loss':
      if a_move == 'Rock':
        b_move = 'Scissors'
      elif a_move == 'Paper':
        b_move = 'Rock'
      elif a_move == 'Scissors':
        b_move = 'Paper'
    elif b_outcome == 'Draw':
      if a_move == 'Rock':
        b_move = 'Rock'
      elif a_move == 'Paper':
        b_move = 'Paper'
      elif a_move == 'Scissors':
        b_move = 'Scissors'
    elif b_outcome == 'Win':
      if a_move == 'Rock':
        b_move = 'Paper'
      elif a_move == 'Paper':
        b_move = 'Scissors'
      elif a_move == 'Scissors':
        b_move = 'Rock'
    shape_score = _SCORE_BY_MOVE[b_move]
    outcome_score = 0
    if a_move != b_move:
      if a_move == 'Rock':
        if b_move == 'Paper':
          outcome_score = 6
      elif a_move == 'Paper':
        if b_move == 'Scissors':
          outcome_score = 6
      elif a_move == 'Scissors':
        if b_move == 'Rock':
          outcome_score = 6
    else:
      outcome_score = 3
    round_score = shape_score + outcome_score
    total_score += round_score
  return total_score


def main() -> None:
  # Part 1
  example_1_data = utils.read_data_as_lines('2022/day_02_example_1.txt')
  print(f'Part 1 Example Answer: {part_1(example_1_data)}')
  data = utils.read_data_as_lines('2022/day_02.txt')
  print(f'Part 1 Actual Answer: {part_1(data)}')
  # Part 2
  example_2_data = utils.read_data_as_lines('2022/day_02_example_2.txt')
  print(f'Part 2 Example Answer: {part_2(example_2_data)}')
  data = utils.read_data_as_lines('2022/day_02.txt')
  print(f'Part 2 Actual Answer: {part_2(data)}')


if __name__ == '__main__':
  utils.create_blank_example_files(day=2, year=2022)
  utils.download_data(day=2, year=2022)
  main()
