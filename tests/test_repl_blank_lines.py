from app.calculator.repl import run_repl, BANNER

def io(seq):
    it = iter(seq)
    out = []
    def _in(_): return next(it)
    def _out(s): out.append(s)
    return _in, _out, out

def test_blank_then_spaces_then_quit_hits_blank_branch():
    _in, _out, out = io(["", "   ", "q"])
    run_repl(_in, _out)
    assert out[0] == BANNER
    assert out[-1] == "Bye!"
