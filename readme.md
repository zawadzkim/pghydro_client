=====
pgHydro_client
=====

PgHydro is a Django based application designed to help manage and distribute data in a hydrological monitoring projects. The data
is stored in a PostgreSQL database hosted through Django Rest Framework API. PgHydro Client is a package based on `requests` library that 
provides a structured and intuitive way to fetch the data from the database and analyse it with ease.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install the repo in your environment

``` cmd
pip install git+https://github.com/zawadzkim/pghydro_client
```

2. Use WaterDataClient class to create connection to the database

``` python
from pghydro_client.client import WaterDataClient
token = 'your-secret-user-token'

client = WaterDataClient('https://www.project-grow.be/api', token)
```

3. Specify what data do you want by providing request parameters:

``` python
# for all methods
timestamp_start = '2021-01-01'  # date format 'YYYY-MM-DD'
timestamp_end = '2021-12-31'  # date format 'YYYY-MM-DD'
station = ['PB15A', 'PB15B', 'PB15C']  # single str or list.

# for physicochemical parameters
parameter = ['pH', 'Temperature', 'Conductivity']

# for analyses
analyte = ['Ca', 'Mg', 'K', 'Na', 'Cl', 'SO4', 'HCO3']
```

4. Fetch the data from the database

``` python
from pghydro_client.client import GetData
# Example for parameters. If no attributes are given, all data on physicochemical parameters will be fetched. This is not 
#  recommended due to possible performance issues in case there is a lot of data on the server.
parameters = GetData(client).get_physicochemical_parameters(parameter=parameter,
                                                            timestamp_start=timestamp_start,
                                                            timestamp_end=timestamp_end,
                                                            station=station)
```

