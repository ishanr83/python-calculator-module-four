from app.calculator.repl import run_repl

def make_io(lines):
    it = iter(lines)
    outs = []
    def input_fn(_):
        return next(it)
    def output_fn(s):
        outs.append(s)
    return input_fn, output_fn, outs

def test_repl_usage_and_numeric_and_divzero():
    input_fn, output_fn, outs = make_io(["add 1","add two 2","div 5 0","exit"])
    run_repl(input_fn, output_fn)
    assert any("Usage:" in s for s in outs)
    assert any("Numbers must be numeric" in s for s in outs)
    assert any("Error: Division by zero" in s for s in outs)
