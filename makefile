#!/bin/sh
venv: venv/bin/activate;

install:
	( \
    test -d venv || virtualenv venv; \
	. venv/bin/activate; \
	pip install pyaudio; \
	pip install pytest; \
	pip install pytest-cov; \
	pip freeze -> requirements.txt ;\
	)

run: venv
	venv/bin/python run.py

test: venv
	venv/bin/pytest --cov=app tests;