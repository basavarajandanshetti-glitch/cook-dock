from cook_bonus import calculate_cook_bonus  # import your cook function

# Test for >=26 present days → 5000
def test_bonus_26():
    assert calculate_cook_bonus(26) == 5000
    assert calculate_cook_bonus(30) == 5000  # edge case above 26

# Test for >=20 present days → 3000
def test_bonus_20():
    assert calculate_cook_bonus(20) == 3000
    assert calculate_cook_bonus(25) == 3000  # edge case below 26

# Test for >=15 present days → 1500
def test_bonus_15():
    assert calculate_cook_bonus(15) == 1500
    assert calculate_cook_bonus(19) == 1500  # edge case below 20

# Test for <15 present days → 0
def test_bonus_10():
    assert calculate_cook_bonus(10) == 0
    assert calculate_cook_bonus(0) == 0      # edge case 0 days
