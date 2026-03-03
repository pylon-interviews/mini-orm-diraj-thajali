default:
	echo "usage: make [all|python|typescript]"

all: python typescript

.PHONY: python
python:
	$(MAKE) -C python

.PHONY: typescript
typescript:
	$(MAKE) -C typescript
