init:
	python3 -m venv env
	test -e main.py || touch main.py
	test -e requirements.txt || touch requirements.txt
	test -e README.md || touch README.md
	test -d .git || git init
	test -e .gitignore || echo "env/" > .gitignore

.PHONY: init
