from app.calculator import __main__ as m

def test_main_runs_repl(monkeypatch):
    called = {"ok": False}
    def fake_run_repl():
        called["ok"] = True
    monkeypatch.setattr(m, "run_repl", fake_run_repl)
    m.main()
    assert called["ok"] is True
