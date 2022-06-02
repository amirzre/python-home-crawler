<h1 align="center"> Home Crawler APP </h1> <br>

<h3 align="center">
  An Crawler to retrieve home information. Built with Python.
</h3>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation Process](#installation-process)

## Introduction

Home crawler provides information about home seller site. Built with Python free to use. Estimate home price with machin learning (scikit-learn).

## Features

A few of the things you can do with this app:

* You can collect home links form home seller site
* Save links to the file or mongo database
* Retrieve home data from stored links
* Store data to file or mongo database
* Estimate home price according home data

## Installation Process

**Installation Process (Linux)**

1. Create a Virtual Environment `python venv venv`
2. Active your Virtual Environment `venv/bin/activate`
3. Activate Virtual Environment `activate`
4. Clone This Project `git clone git@github.com:zanull/python-home-crawler.git`
5. Go To Project Directory `cd python-home-crawler`
6. Install Required Package `pip install -r requirements.txt`
8. Run The Project To Retrieve Home Links `python main.py find_links`
9. Run The Project To Retrieve Home Data `python main.py extract_data`
