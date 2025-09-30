from app.calculator.repl import run_repl, BANNER
from app.calculation.factory import _reset_history_for_tests

def io(seq):
    it = iter(seq)
    out = []
    def _in(_): return next(it)
    def _out(s): out.append(s)
    return _in, _out, out

def test_empty_input_then_quit_covers_continue():
    # Covers the "if not line: continue" path (lines ~26-28)
    _in, _out, out = io(["", "q"])
    run_repl(_in, _out)
    assert out[0] == BANNER
    assert out[-1] == "Bye!"

def test_history_when_empty_and_help_covers_branches():
    # Ensure empty history first, then exercise 'history' and 'help'
    _reset_history_for_tests()
    _in, _out, out = io(["history", "help", "q"])
    run_repl(_in, _out)
    assert any("No calculations yet." in s for s in out)
    assert any("Commands:" in s for s in out)

def test_unknown_command_branch_and_divzero_message():
    # Covers "Unknown command" branch (line ~48) and division-by-zero path
    _in, _out, out = io(["foo", "div 5 0", "q"])
    run_repl(_in, _out)
    assert any("Unknown command" in s for s in out)
    assert any("Error: Division by zero" in s for s in out)
