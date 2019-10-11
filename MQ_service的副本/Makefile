HOSTNAME := $(shell hostname -f)
SUBDIR = $(shell ls -d */)

test_units := $(patsubst %/,%,$(SUBDIR))

all:
	@echo "use 'make tests' to run all tests'"
	@echo "use 'make update' to update all docker images"
	@echo "use 'make TEST' to run individual test: ${test_units}"
	@echo "use 'make status' to get general info of  the container images"

.PHONY: $(test_units)
$(test_units): 
	$@/$@.sh

.PHONY: update
update:
	./update.sh "$(test_units)"

.NOTPARALLEL: tests
tests: $(test_units)

.PHONY: status
status:
	./status.sh "$(test_units)"
