#!/bin/sh
rm -rf dist
python3 setup.py bdist_wheel
twine upload dist/*