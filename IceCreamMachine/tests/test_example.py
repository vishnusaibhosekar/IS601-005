import pytest
from IcecreamMachine import IceCreamMachine, STAGE, ExceededRemainingChoicesException, OutOfStockException

@pytest.fixture
def machine():
    return IceCreamMachine()

@pytest.fixture
def machine1():
    return IceCreamMachine()

@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(2.00,2.00)
    return machine
    
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(2.00,2.00)
    return machine

def test_production_line(second_order):
    assert second_order is not None

# UCID: vb434
# Date: 10/23/2022
def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Container.name

# UCID: vb434
# Date: 10/23/2022
def test_flavour_in_stock(machine):
    # setting available quantity to 1 for testing convenience
    machine.flavors[0].quantity = 1
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    try:
        machine.handle_flavor("vanilla")
        assert machine.flavors[0].quantity == -1
    except OutOfStockException:
        assert False

# UCID: vb434
# Date: 10/23/2022
def test_toppings_in_stock(machine):
    # setting available quantity to 1 for testing convenience
    machine.toppings[0].quantity = 1
    machine.handle_container("cup")
    machine.handle_flavor("next")
    machine.handle_toppings("sprinkles")
    try:
        machine.handle_toppings("sprinkles")
        assert machine.toppings[0].quantity == -1
    except OutOfStockException:
        assert False

# UCID: vb434
# Date: 10/23/2022
def test_max_scoops(machine):
    machine.handle_container("cup")
    # loop to choose (maximum - 1) number of scoops
    for _ in range(machine.MAX_SCOOPS - 1):
        machine.handle_flavor("chocolate")
    try:
        machine.handle_flavor("chocolate")
        assert machine.remaining_scoops == 0
    except ExceededRemainingChoicesException:
        assert False

# UCID: vb434
# Date: 10/23/2022
def test_max_toppings(machine):
    machine.handle_container("cup")
    machine.handle_flavor("next")
    # loop to choose (maximum - 1) number of toppings
    for _ in range(machine.MAX_TOPPINGS - 1):
        machine.handle_toppings("peanuts")
    try:
        machine.handle_toppings("peanuts")
        assert machine.remaining_toppings == 0
    except ExceededRemainingChoicesException:
        assert False

# UCID: vb434
# Date: 10/23/2022
def test_total_cost(machine1):
    machine1.handle_container("cup")
    machine1.handle_flavor("vanilla")
    machine1.handle_flavor("chocolate")
    machine1.handle_flavor("strawberry")
    machine1.handle_flavor("next")
    machine1.handle_toppings("sprinkles")
    machine1.handle_toppings("chocolate chips")
    machine1.handle_toppings("m&ms")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == '4.75'

# UCID: vb434
# Date: 10/23/2022
def test_total_sales(machine1):
    machine1.handle_container("cup")
    machine1.handle_flavor("vanilla")
    machine1.handle_flavor("chocolate")
    machine1.handle_flavor("next")
    machine1.handle_toppings("done")
    iceCreamCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost1, iceCreamCost1)

    machine1.handle_container("waffle cone")
    machine1.handle_flavor("strawberry")
    machine1.handle_flavor("next")
    machine1.handle_toppings("chocolate chips")
    machine1.handle_toppings("m&ms")
    machine1.handle_toppings("done")
    iceCreamCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost2, iceCreamCost2)

    assert machine1.total_sales == iceCreamCost1 + iceCreamCost2

# UCID: vb434
# Date: 10/23/2022
def test_total_icecreams(second_order, machine1):
    machine1.handle_container("cup")
    machine1.handle_flavor("chocolate")
    machine1.handle_flavor("next")
    machine1.handle_toppings("done")
    iceCreamCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost1, iceCreamCost1)

    machine1.handle_container("waffle cone")
    machine1.handle_flavor("next")
    machine1.handle_toppings("m&ms")
    machine1.handle_toppings("done")
    iceCreamCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost2, iceCreamCost2)

    machine1.handle_container("sugar cone")
    machine1.handle_flavor("next")
    machine1.handle_toppings("peanuts")
    machine1.handle_toppings("done")
    iceCreamCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost3, iceCreamCost3)

    assert second_order.total_icecreams == 2 and machine1.total_icecreams == 3