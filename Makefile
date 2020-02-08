# --------------------------------------------------------------------
# There should be no need to change this,
# if you do you'll also need to update docker-compose.yml
# --------------------------------------------------------------------

SERVICE_TARGET := pyshipper

# retrieve NAME from /variables.py file
MODULE_NAME = \
	$(shell awk -F= '/^NAME\ ?=/{gsub(/\47|"/, "", $$NF);print $$NF;exit}' variables)
MODULE_VERSION = \
	$(shell awk -F= '/^VERSION\ ?=/{gsub(/\47|"/, "", $$NF);print $$NF;exit}' variables)

export MODULE_NAME

.PHONY: build
build:
	python setup.py sdist

.PHONY: pylint
pylint:
	cd ./markd && pylint --output-format=text * -f parseable

.PHONY: test
test:
	python markd/main/tests/unit.py -v

.PHONY: upload
upload:
	twine upload ./dist/$(MODULE_NAME)-$(MODULE_VERSION)*

.PHONY: clean
clean:
	rm -rf ./build ./dist ./*.egg-info 
