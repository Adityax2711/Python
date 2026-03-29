## Repo overview

This is a small learning/training Python workspace containing simple example scripts and two calculator programs:
- `basic.py` — assorted beginner examples (variables, types, control flow). Good for quick snippets or teaching edits.
- `calculator.py` — a simple interactive CLI calculator (add/sub/mul/div). Functions are defined at top-level and the script runs interactively when executed.
- `Scientificcalculator.py` — a larger CLI calculator that mixes basic arithmetic with math trig/log/root functions; it imports `math` and (unused) `requests`.
- `firstproject.py` — a number-guessing interactive script (random + input loop).
- `music.py` — prints lyrics with timed character output; contains small unrelated demos.

## What an AI coding agent should know (concise)

- These files are lightweight single-file scripts, not a packaged Python project. There is no `requirements.txt`, `setup.py`, or tests directory. Changes should preserve the simple CLI behavior and avoid adding heavy framework assumptions.
- Editing a file should keep it runnable as `python <file>.py` from the repository root. Assume Windows PowerShell as the primary shell for CLI examples.
- Prefer minimal, non-breaking improvements: clear function boundaries, input validation, error messages, and fix obvious typos (for example `print("hello worrld")` in `firstproject.py`).
- Do not introduce network calls or new dependencies unless the user asks. `Scientificcalculator.py` imports `requests` but never uses it — flag and remove or ask before adding network behavior.
## Project-specific patterns & quick examples

- Interactive CLI pattern: read input via `input()` then compute and `print()` result. Example: `calculator.py` defines `add/subtract/multiply/divide` then asks for `choice` and two numbers.
- Math helpers live in the same file as the CLI logic (no modules). If extracting helpers, keep them importable and add a small `if __name__ == "__main__":` runner to preserve CLI behavior.
- Trigonometric helpers in `Scientificcalculator.py` expect degree inputs and convert to radians using `math.radians(...)`. Keep that convention when refactoring.
- Error/edge cases frequently unhandled: non-numeric input, division by zero (some handling exists), invalid menu choices. Add targeted, conservative input validation where helpful.

## Safe change guidelines for the AI

1. Preserve interactive behavior by adding `if __name__ == "__main__":` when converting scripts to importable modules.
2. Keep third-party imports out unless a corresponding `requirements.txt` or user confirmation is provided. Example: remove unused `requests` from `Scientificcalculator.py` or confirm its purpose.
3. When refactoring, add a tiny test or example-run comment at the bottom of the new module showing sample usage.
4. Use clear, readable names and fix obvious typos (e.g., `hello worrld` → `hello world`).

## Files to reference when making edits

- `calculator.py` — canonical example for simple arithmetic functions and interactive menu wiring.
- `Scientificcalculator.py` — shows math usage, degree→radian convention, and several unimplemented/incorrect trig helpers (e.g., attempts to call `math.cot` / `math.cosec` which do not exist). If fixing, implement cot/sec/cosec manually or use reciprocals of tan/sin/cos.
- `basic.py` & `music.py` — small demos; useful for stylistic consistency and simple I/O examples.

## Example actionable tasks the agent can perform

- Small bug fixes: correct typos, implement missing trig functions in `Scientificcalculator.py` using existing `math` primitives, and remove unused imports.
- Make modules import-safe: wrap CLI code with `if __name__ == "__main__":` and expose functions at top-level for reuse.
- Add minimal input validation to calculators (validate numeric inputs and menu choices) and keep messages concise.

## What not to change without asking

- The overall interactive, educational tone and simple CLI flow of scripts.
- Introducing a project-level dependency file or tests without the user's sign-off.

---
Please review these instructions and tell me any additional project conventions or goals (packaging, tests, target Python version) you want the AI to follow. I'll iterate the file accordingly.
