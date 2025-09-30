from app.calculator.repl import run_repl, BANNER, PROMPT

def make_io(lines):
    it = iter(lines)
    outs = []
    def input_fn(_): return next(it)
    def output_fn(s): outs.append(s)
    return input_fn, output_fn, outs

def test_banner_and_quit_cover():
    input_fn, output_fn, outs = make_io(["q"])
    run_repl(input_fn, output_fn)
    assert outs[0] == BANNER
    assert outs[-1] == "Bye!"
    assert PROMPT == "> "
