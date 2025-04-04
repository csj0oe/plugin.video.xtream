VENV = ../.venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: run clean

run: $(VENV)/bin/activate
	$(PYTHON) default.py

package:
	cd .. && rm -fr xtream-*.zip && zip -r xtream-$$(date +%s).zip plugin.video.xtream -x plugin.video.xtream/.git/**\* -x plugin.video.xtream/temp/**\* -x plugin.video.xtream/__pycache__/**\*


$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf __pycache__
	rm -rf $(VENV)