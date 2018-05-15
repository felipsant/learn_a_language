#!/bin/sh
venv: venv/bin/activate;

install:
	( \
    test -d venv || virtualenv venv; \
	. venv/bin/activate; \
	pip install pyaudio; \
	pip install cython==0.25.2; \
	pip install kivy; \
	pip install pytest; \
	pip install pytest-cov; \
	pip freeze -> requirements.txt ;\
	)

run: venv
	venv/bin/python run.py 0

test: venv
	venv/bin/pytest --cov=app tests;

new_guid: venv
	venv/bin/python new_guid.py

build: 
	docker build .