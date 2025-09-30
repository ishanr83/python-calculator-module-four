# Author: Ishan Rehan | Date: 2025-09-29
from typing import Callable
from app.calculation.factory import CalculationFactory, history, operations_map

PROMPT = "> "
BANNER = "Calculator REPL. Commands: add|sub|mul|div <a> <b>  | history | help | exit"

def _help_text() -> str:
    ops = "|".join(sorted(operations_map().keys()))
    return f"Commands: {ops} <a> <b>  | history | help | exit"

def _parse_two_numbers(parts: list[str]) -> tuple[float, float]:
    if len(parts) != 3:
        raise ValueError("Usage: <op> <num1> <num2>")
    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError:
        raise ValueError("Numbers must be numeric")
    return a, b

def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    output_fn(BANNER)
    while True:
        try:
            raw = input_fn(PROMPT)
        except (EOFError, KeyboardInterrupt):  # pragma: no cover (hard to simulate portably)
            output_fn("Bye!")
            break

        line = "" if raw is None else str(raw).strip()
        parts = line.split()

        # Blank or whitespace lines act like 'help' — no separate continue branch.
        if not parts:
            output_fn(_help_text())
            continue

        cmd = parts[0].lower()

        if cmd in {"exit", "quit", "q"}:
            output_fn("Bye!")
            break

        if cmd == "help":
            output_fn(_help_text())
            continue

        if cmd == "history":
            items = history()
            if not items:
                output_fn("No calculations yet.")
            else:
                for i, c in enumerate(items, 1):
                    try:
                        result = c.execute()
                        output_fn(f"{i}. {c.op_name} {c.a} {c.b} = {result}")
                    except ZeroDivisionError:
                        output_fn(f"{i}. {c.op_name} {c.a} {c.b} = Error: Division by zero")
            continue

        if cmd in operations_map():
            try:
                a, b = _parse_two_numbers(parts)
                calc = CalculationFactory.from_parts(cmd, a, b)
                try:
                    result = calc.execute()
                    output_fn(str(result))
                except ZeroDivisionError:
                    output_fn("Error: Division by zero")
            except ValueError as e:
                output_fn(f"Error: {e}")
        else:
            output_fn("Unknown command. Use help for usage.")
