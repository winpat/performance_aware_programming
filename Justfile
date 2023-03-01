alias g := generate-data
alias b := benchmark

generate-data NUM_POINTS:
	python -m haversine.data_generator {{NUM_POINTS}}

benchmark:
	pytest --benchmark-only