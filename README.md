# Python Import Calculating Assistant (web edition!)

PyICA is an import calculating assistant for [EvE Online](https://www.eveonline.com/) that aims to help marketeers make 
a profit and maintain their markets stocked.

## Installing requirements

This project assumes that `rabbitmq-server` is running on `localhost` using default configs.
On Ubuntu:

`$ sudo apt-get install rabbitmq-server`

Please install all Python dependencies.

`$ pip install -r requirements.txt`

## Contents
### Existing Features:
`pyica_web/`: Root of the project. Contains config files for PyICA, Django and Celery.

`import_calculator/`: Table that shows raw market data along with some computed stats to help you decide what to import 
to your home market.

### Coming soon: 
`predictive_analytics/`: Creates predictive demand analytics based on already existing markets in EvE online.

`fitting_calculator/`: Creates a shopping list to build fits in the cheapest way possible. Lists which modules to import 
and/or source locally based on markets selected.
