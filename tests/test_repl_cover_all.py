from app.calculator.repl import run_repl, BANNER
from app.calculation.factory import _reset_history_for_tests

def io(seq):
    it = iter(seq)
    out = []
    def _in(_): return next(it)
    def _out(s): out.append(s)
    return _in, _out, out

def test_empty_input_continue_and_quit():
    # Hits "if not line: continue" (lines ~26-28)
    _in, _out, out = io(["", "", "q"])
    run_repl(_in, _out)
    assert out[0] == BANNER
    assert out[-1] == "Bye!"

def test_unknown_command_then_quit():
    # Hits the "Unknown command" branch (line ~64)
    _in, _out, out = io(["foo", "q"])
    run_repl(_in, _out)
    assert any("Unknown command" in s for s in out)

def test_history_empty_then_help_then_quit():
    # Ensures "No calculations yet." is printed
    _reset_history_for_tests()
    _in, _out, out = io(["history", "help", "q"])
    run_repl(_in, _out)
    assert any("No calculations yet." in s for s in out)
    assert any("Commands:" in s for s in out)

def test_history_shows_success_and_divzero_entries():
    # Cover history loop for both success and ZeroDivisionError
    _reset_history_for_tests()
    _in, _out, out = io([
        "add 2 3",     # success
        "div 5 0",     # triggers ZeroDivisionError in immediate command, but still stored
        "history",     # prints both; second triggers except ZeroDivisionError inside loop
        "q"
    ])
    run_repl(_in, _out)
    assert "5.0" in out
    assert any(s == "Error: Division by zero" for s in out)
    assert any("add 2.0 3.0 = 5.0" in s for s in out)
    assert any("div 5.0 0.0 = Error: Division by zero" in s for s in out)
