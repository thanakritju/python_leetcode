# make test problem=224
test:
	python3 -m unittest discover ${problem} "*_test.py"