from app.calculator.repl import run_repl, BANNER

def io(seq):
    it = iter(seq)
    out = []
    def _in(_): return next(it)
    def _out(s): out.append(s)
    return _in, _out, out

def test_blank_then_spaces_route_to_help_and_quit():
    _in, _out, out = io(["", "   ", "q"])
    run_repl(_in, _out)
    assert out[0] == BANNER
    assert any("Commands:" in s for s in out)  # help printed for blank
    assert out[-1] == "Bye!"
