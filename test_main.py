from calc import add, sub, mul, div

def test_add():
	assert add(1,1) == 3
def test_sub():
	assert sub(5,3) == 2
def test_mul():
	assert mul(2,6) == 12
def test_div():
	assert div(6,3) == 2