python = `which python3.6`
script = "totd.py"
pager = "cowsay -f hellokitty"

# Run as intended, with no arguments through a pager.
run:
	{{python}} ./{{script}} | {{pager}}

# Lint and format the source code.
lint-python:
	cp ./{{script}} /tmp/{{script}}.backup
	autopep8 --in-place ./{{script}}
	pylint ./{{script}}

# Lint the YAML tip data.
lint-yaml:
	yamllint .

# Check for any broken URLs in documentation.
lint-docs:
	linkcheck -e md,txt -c "200,301"

# Lint everything.
lint: lint-python lint-yaml lint-docs

# Install all dependencies.
install-deps:
	pip install -r requirements.txt

# Push everything to our official GitHub repository.
push:
	git push --all origin

# Fetch all updates from our GitHub repository.
fetch:
	git fetch --tags --prune origin

# Display the help output.
help:
	{{python}} ./{{script}} --help
