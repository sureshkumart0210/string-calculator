# String Calculator TDD Kata

Implementation of the String Calculator Kata using Test-Driven Development (TDD).  
This was built as part of the Incubyte hiring process.

## Steps followed
- Started with the simplest test (empty string) and incrementally added more tests.
- Followed TDD cycle: **Red → Green → Refactor**.
- Made small, frequent commits to show code evolution.

## Features
- Empty string returns `0`
- Single number returns its value
- Comma-separated numbers are summed
- Any amount of numbers supported
- Newlines allowed as separators (`"1\n2,3" => 6`)
- Custom delimiters supported (`"//;\n1;2" => 3`)
- Negative numbers raise exception with all negatives listed

## Run Tests
```bash
pip install -r requirements.txt
pytest -q
