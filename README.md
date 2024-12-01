# Advent of Code Solutions

- Session cookie expected location:
  - `~/.config/aocd/token`
- Generate template script for a particular day:
  - `uv run make_day_script.py 1 2024`
- Run solution code for a particular day:
  - `uv run -m 2024.day_01`
- Run formater: 
  - `uv run ruff check --select I --fix && uv run ruff format`
- Run type checking: 
  - `uv run mypy 2024/day_01.py`
