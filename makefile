# make test problem=0224
test:
	python3 -m unittest discover ${problem} "*_test.py"