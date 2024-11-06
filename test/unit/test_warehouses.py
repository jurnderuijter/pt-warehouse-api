import pytest
from providers import data_provider


@pytest.fixture
def _warehouses():
    data_provider.init()
    return data_provider.fetch_warehouse_pool()


def test_get_warehouse(_warehouses):
    # Existing
    warehouse = _warehouses.get_warehouse(warehouse_id=1)
    assert "YQZZNL56" == warehouse["code"]
