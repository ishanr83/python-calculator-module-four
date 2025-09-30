import pytest
from app.calculation.factory import CalculationFactory, history, operations_map

def test_operations_map_has_all_ops():
    ops = operations_map()
    for k in ("add","sub","mul","div"):
        assert k in ops and callable(ops[k])

def test_factory_and_history_positive():
    before = len(history())
    c = CalculationFactory.from_parts("add", 2, 3)
    assert c.execute() == 5
    assert len(history()) == before + 1

def test_factory_unknown_op_raises():
    with pytest.raises(ValueError):
        CalculationFactory.from_parts("pow", 2, 3)

def test_factory_div_zero_path():
    c = CalculationFactory.from_parts("div", 1, 0)
    with pytest.raises(ZeroDivisionError):
        _ = c.execute()
