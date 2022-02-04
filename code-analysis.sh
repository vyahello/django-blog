#!/usr/bin/env bash

PROJECT="web_site"


function check-black() {
  black --check "${PROJECT}"
}


function check-isort() {
  isort "${PROJECT}" --check-only --verbose
}


function main() {
  check-black && check-isort
}


main
