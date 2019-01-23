#!/usr/bin/env bash

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
pipenv run flask run --host=0.0.0.0
