### Hexlet tests and linter status:
[![Actions Status](https://github.com/berteek/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/berteek/python-project-49/actions)

<a href="https://codeclimate.com/github/berteek/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/fa7aaa99b817393e160e/maintainability" /></a>

## Description
A collection of small brain-games using CLI.

## Requirements
python 3.11+
poetry
pip

## Installation
Clone this repository and run
```
make package-install
```
Then build it with poetry by running
```
make build
```
Install built package into the system
```
make package-install
```

## Usage
There are 5 games total: 
- Check if give number is even
```
make brain-even
```
- Calculate expression
```
make brain-calc
```
- Find greatest common divisor
```
make brain-gcd
```
- Find missing number in progression
```
make brain-progression
```
- Check if given number is prime
```
make brain-prime
```
