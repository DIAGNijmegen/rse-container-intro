#! /bin/bash

jupyter-nbconvert --to slides docker-intro.ipynb --reveal-prefix=reveal.js --post serve

