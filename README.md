## climetlab_wekeo_ecmwf

A dataset plugin for climetlab for the ECMWF datasets available on WEkEO.

> **Note**
> This plugin is currently in beta stage and not yet available on Pypi nor Conda.
> Please follow the installation instruction as "pip install" or "conda install" won't work.

Installation
------------
To install the plugin, clone the GitHub repository on the target machine.
Once done, activate the Python virtual environment or the Conda environment, depending on the tool you have chosen, and then run:

    cd climentlab-wekeo-ecmwf
    pip install .

Features
--------

This plugin provides a simple access to ECMWF datasets provided by WEkEO.

Each dataset presents a number of variables to narrow down the data to download.

Those variables and the range of accepted values can be inspected directly in the code.

While it is not mandatory, the usage of Dask is recommended.

For usage examples, please refer to the [demo notebook](https://github.com/wekeo/climetlab-wekeo-ecmwf/tree/main/notebooks/demo_main.ipynb)

## Datasets description

There are several datasets:

- wekeo-ecmwf-cams-europe-air-quality-forecasts
- wekeo-ecmwf-cams-europe-air-quality-reanalyses
- wekeo-ecmwf-cams-global-atmospheric-composition-forecasts
- wekeo-ecmwf-cams-global-fire-emissions-gfas
- wekeo-ecmwf-cams-global-ghg-reanalysis-egg4-monthly
- wekeo-ecmwf-cams-global-greenhouse-gas-inversion
- wekeo-ecmwf-cams-global-reanalysis-eac4-monthly
- wekeo-ecmwf-cams-global-reanalysis-eac4
- wekeo-ecmwf-cams-solar-radiation-timeseries
- wekeo-ecmwf-cems-fire-historical
- wekeo-ecmwf-cems-glofas-forecast
- wekeo-ecmwf-cems-glofas-historical
- wekeo-ecmwf-cems-glofas-reforecast
- wekeo-ecmwf-cems-glofas-seasonal-reforecast
- wekeo-ecmwf-cems-glofas-seasonal
- wekeo-ecmwf-efas-forecast
- wekeo-ecmwf-efas-historical
- wekeo-ecmwf-efas-reforecast
- wekeo-ecmwf-efas-seasonal-reforecast
- wekeo-ecmwf-efas-seasonal
- wekeo-ecmwf-insitu-glaciers-elevation-mass
- wekeo-ecmwf-insitu-glaciers-extent
- wekeo-ecmwf-insitu-gridded-observations-nordic
- wekeo-ecmwf-reanalysis-era5-land-monthly-means
- wekeo-ecmwf-reanalysis-era5-land
- wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means-preliminary-back-extension
- wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means
- wekeo-ecmwf-reanalysis-era5-pressure-levels-preliminary-back-extension
- wekeo-ecmwf-reanalysis-era5-pressure-levels
- wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means-preliminary-back-extension
- wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means
- wekeo-ecmwf-reanalysis-era5-single-levels-preliminary-back-extension
- wekeo-ecmwf-reanalysis-era5-single-levels
- wekeo-ecmwf-reanalysis-uerra-europe-height-levels
- wekeo-ecmwf-reanalysis-uerra-europe-pressure-levels
- wekeo-ecmwf-reanalysis-uerra-europe-single-levels
- wekeo-ecmwf-reanalysis-uerra-europe-soil-levels
- wekeo-ecmwf-satellite-carbon-dioxide
- wekeo-ecmwf-satellite-earth-radiation-budget
- wekeo-ecmwf-satellite-methane
- wekeo-ecmwf-satellite-precipitation-microwave
- wekeo-ecmwf-satellite-sea-ice-edge-type
- wekeo-ecmwf-satellite-sea-level-black-sea
- wekeo-ecmwf-satellite-sea-level-global
- wekeo-ecmwf-satellite-sea-level-mediterranean
- wekeo-ecmwf-satellite-soil-moisture
- wekeo-ecmwf-satellite-surface-radiation-budget
- wekeo-ecmwf-satellite-total-column-water-vapour-land-ocean
- wekeo-ecmwf-satellite-total-column-water-vapour-ocean
- wekeo-ecmwf-satellite-upper-troposphere-humidity
- wekeo-ecmwf-seasonal-monthly-pressure-levels
- wekeo-ecmwf-seasonal-monthly-single-levels
- wekeo-ecmwf-seasonal-original-pressure-levels
- wekeo-ecmwf-seasonal-original-single-levels
- wekeo-ecmwf-seasonal-postprocessed-pressure-levels
- wekeo-ecmwf-seasonal-postprocessed-single-levels
- wekeo-ecmwf-sis-agrometeorological-indicators
- wekeo-ecmwf-sis-biodiversity-cmip5-global
- wekeo-ecmwf-sis-biodiversity-cmip5-regional
- wekeo-ecmwf-sis-biodiversity-era5-global
- wekeo-ecmwf-sis-biodiversity-era5-regional
- wekeo-ecmwf-sis-ecv-cmip5-bias-corrected
- wekeo-ecmwf-sis-european-risk-extreme-precipitation-indicators
- wekeo-ecmwf-sis-european-risk-flood-indicators
- wekeo-ecmwf-sis-european-wind-storm-indicators
- wekeo-ecmwf-sis-european-wind-storm-synthetic-events
- wekeo-ecmwf-sis-health-vector
- wekeo-ecmwf-sis-heat-and-cold-spells
- wekeo-ecmwf-sis-hydrology-meteorology-derived-projections
- wekeo-ecmwf-sis-hydrology-variables-derived-projections
- wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-forecast
- wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-reforecast
- wekeo-ecmwf-sis-marine-properties
- wekeo-ecmwf-sis-shipping-arctic
- wekeo-ecmwf-sis-shipping-consumption-on-routes
- wekeo-ecmwf-sis-temperature-statistics
- wekeo-ecmwf-sis-urban-climate-cities
- wekeo-ecmwf-sis-water-hydrological-change

The descriptions can be retrieved directly from [WEkEO](https://www.wekeo.eu/data)


## Using climetlab to access the data

See the [demo notebooks](https://github.com/wekeo/climetlab-wekeo-ecmwf/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wekeo/climetlab-wekeo-ecmwf/main?urlpath=lab)


- [demo_main.ipynb](https://github.com/wekeo/climetlab-wekeo-ecmwf/tree/main/notebooks/demo_main.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/wekeo/climetlab-wekeo-ecmwf/blob/main/notebooks/demo_main.ipynb)
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wekeo/climetlab-wekeo-ecmwf/blob/main/notebooks/demo_main.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wekeo/climetlab-wekeo-ecmwf/main?filepath=notebooks/demo_main.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/wekeo/climetlab-wekeo-ecmwf/tree/main/notebooks/demo_main.ipynb)



The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-wekeo-ecmwf
import climetlab as cml
ds = cml.load_dataset(
    "wekeo-ecmwf-sis-water-hydrological-change",
    variable=[
        "air_temperature",
        "volumetric_soil_moisture",
        "precipitation"
    ],
    time_aggregation=["autumn", "spring"],
    format_="zip",
    gcm_model="esm_chem",
    statistic="change_in_the_annual_mean",
    experiment="rcp_8_5",
    hydrological_model="pcr_globwb",
)
ds.to_xarray()

LICENSE
-------

See the LICENSE file.
(C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
This software is licensed under the terms of the Apache Licence Version 2.0
which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
In applying this licence, ECMWF does not waive the privileges and immunities
granted to it by virtue of its status as an intergovernmental organisation
nor does it submit to any jurisdiction.

Authors
-------

Germano Guerrini and al.

See also the CONTRIBUTORS.md file.
