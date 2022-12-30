#!/usr/bin/env bash
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:application --master --processes 5 --threads 8 --reload-on-exception


