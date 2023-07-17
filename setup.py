#!/usr/bin/env python
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_wekeo_ecmwf"  # noqa: E501

version = None
lines = read(f"{package_name}/version").split("\n")
if lines:
    version = lines[0]

assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description=(
        "A dataset plugin for climetlab for the dataset climetlab-wekeo-ecmwf"  # noqa: E501
    ),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Germano Guerrini",
    author_email="germano.guerrini@exprivia.com",
    url="https://github.com/wekeo/climetlab-wekeo-ecmwf",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "climetlab>=0.10.0",
        "climetlab-wekeo-source",
    ],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            # End-users will use cml.load_dataset("climetlab-wekeo-ecmwf", ...)
            # see the tests/ folder for a example.
            "wekeo-ecmwf-cams-europe-air-quality-forecasts=climetlab_wekeo_ecmwf.cams_europe_air_quality_forecasts:cams_europe_air_quality_forecasts",
            "wekeo-ecmwf-cams-europe-air-quality-reanalyses=climetlab_wekeo_ecmwf.cams_europe_air_quality_reanalyses:cams_europe_air_quality_reanalyses",
            "wekeo-ecmwf-cams-global-atmospheric-composition-forecasts=climetlab_wekeo_ecmwf.cams_global_atmospheric_composition_forecasts:cams_global_atmospheric_composition_forecasts",
            "wekeo-ecmwf-cams-global-emission-inventories=climetlab_wekeo_ecmwf.cams_global_emission_inventories:cams_global_emission_inventories",
            "wekeo-ecmwf-cams-global-fire-emissions-gfas=climetlab_wekeo_ecmwf.cams_global_fire_emissions_gfas:cams_global_fire_emissions_gfas",
            "wekeo-ecmwf-cams-global-ghg-reanalysis-egg4-monthly=climetlab_wekeo_ecmwf.cams_global_ghg_reanalysis_egg4_monthly:cams_global_ghg_reanalysis_egg4_monthly",
            "wekeo-ecmwf-cams-global-ghg-reanalysis-egg4=climetlab_wekeo_ecmwf.cams_global_ghg_reanalysis_egg4:cams_global_ghg_reanalysis_egg4",
            "wekeo-ecmwf-cams-global-greenhouse-gas-inversion=climetlab_wekeo_ecmwf.cams_global_greenhouse_gas_inversion:cams_global_greenhouse_gas_inversion",
            "wekeo-ecmwf-cams-global-radiative-forcing-auxilliary-variables=climetlab_wekeo_ecmwf.cams_global_radiative_forcing_auxilliary_variables:cams_global_radiative_forcing_auxilliary_variables",
            "wekeo-ecmwf-cams-global-radiative-forcings=climetlab_wekeo_ecmwf.cams_global_radiative_forcings:cams_global_radiative_forcings",
            "wekeo-ecmwf-cams-global-reanalysis-eac4-monthly=climetlab_wekeo_ecmwf.cams_global_reanalysis_eac4_monthly:cams_global_reanalysis_eac4_monthly",
            "wekeo-ecmwf-cams-global-reanalysis-eac4=climetlab_wekeo_ecmwf.cams_global_reanalysis_eac4:cams_global_reanalysis_eac4",
            "wekeo-ecmwf-cams-solar-radiation-timeseries=climetlab_wekeo_ecmwf.cams_solar_radiation_timeseries:cams_solar_radiation_timeseries",
            "wekeo-ecmwf-cems-fire-historical=climetlab_wekeo_ecmwf.cems_fire_historical:cems_fire_historical",
            "wekeo-ecmwf-cems-glofas-forecast=climetlab_wekeo_ecmwf.cems_glofas_forecast:cems_glofas_forecast",
            "wekeo-ecmwf-cems-glofas-historical=climetlab_wekeo_ecmwf.cems_glofas_historical:cems_glofas_historical",
            "wekeo-ecmwf-cems-glofas-reforecast=climetlab_wekeo_ecmwf.cems_glofas_reforecast:cems_glofas_reforecast",
            "wekeo-ecmwf-cems-glofas-seasonal-reforecast=climetlab_wekeo_ecmwf.cems_glofas_seasonal_reforecast:cems_glofas_seasonal_reforecast",
            "wekeo-ecmwf-cems-glofas-seasonal=climetlab_wekeo_ecmwf.cems_glofas_seasonal:cems_glofas_seasonal",
            "wekeo-ecmwf-efas-forecast=climetlab_wekeo_ecmwf.efas_forecast:efas_forecast",
            "wekeo-ecmwf-efas-historical=climetlab_wekeo_ecmwf.efas_historical:efas_historical",
            "wekeo-ecmwf-efas-reforecast=climetlab_wekeo_ecmwf.efas_reforecast:efas_reforecast",
            "wekeo-ecmwf-efas-seasonal-reforecast=climetlab_wekeo_ecmwf.efas_seasonal_reforecast:efas_seasonal_reforecast",
            "wekeo-ecmwf-efas-seasonal=climetlab_wekeo_ecmwf.efas_seasonal:efas_seasonal",
            "wekeo-ecmwf-insitu-glaciers-elevation-mass=climetlab_wekeo_ecmwf.insitu_glaciers_elevation_mass:insitu_glaciers_elevation_mass",
            "wekeo-ecmwf-insitu-glaciers-extent=climetlab_wekeo_ecmwf.insitu_glaciers_extent:insitu_glaciers_extent",
            "wekeo-ecmwf-insitu-gridded-observations-nordic=climetlab_wekeo_ecmwf.insitu_gridded_observations_nordic:insitu_gridded_observations_nordic",
            "wekeo-ecmwf-reanalysis-era5-land-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_land_monthly_means:reanalysis_era5_land_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-land=climetlab_wekeo_ecmwf.reanalysis_era5_land:reanalysis_era5_land",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means-preliminary-back-extension=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels_monthly_means_preliminary_back_extension:reanalysis_era5_pressure_levels_monthly_means_preliminary_back_extension",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels_monthly_means:reanalysis_era5_pressure_levels_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels-preliminary-back-extension=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels_preliminary_back_extension:reanalysis_era5_pressure_levels_preliminary_back_extension",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels:reanalysis_era5_pressure_levels",
            "wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means-preliminary-back-extension=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels_monthly_means_preliminary_back_extension:reanalysis_era5_single_levels_monthly_means_preliminary_back_extension",
            "wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels_monthly_means:reanalysis_era5_single_levels_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-single-levels-preliminary-back-extension=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels_preliminary_back_extension:reanalysis_era5_single_levels_preliminary_back_extension",
            "wekeo-ecmwf-reanalysis-era5-single-levels=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels:reanalysis_era5_single_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-height-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_height_levels:reanalysis_uerra_europe_height_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_pressure_levels:reanalysis_uerra_europe_pressure_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-single-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_single_levels:reanalysis_uerra_europe_single_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-soil-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_soil_levels:reanalysis_uerra_europe_soil_levels",
            "wekeo-ecmwf-satellite-carbon-dioxide=climetlab_wekeo_ecmwf.satellite_carbon_dioxide:satellite_carbon_dioxide",
            "wekeo-ecmwf-satellite-earth-radiation-budget=climetlab_wekeo_ecmwf.satellite_earth_radiation_budget:satellite_earth_radiation_budget",
            "wekeo-ecmwf-satellite-methane=climetlab_wekeo_ecmwf.satellite_methane:satellite_methane",
            "wekeo-ecmwf-satellite-precipitation-microwave=climetlab_wekeo_ecmwf.satellite_precipitation_microwave:satellite_precipitation_microwave",
            "wekeo-ecmwf-satellite-sea-ice-edge-type=climetlab_wekeo_ecmwf.satellite_sea_ice_edge_type:satellite_sea_ice_edge_type",
            "wekeo-ecmwf-satellite-sea-level-black-sea=climetlab_wekeo_ecmwf.satellite_sea_level_black_sea:satellite_sea_level_black_sea",
            "wekeo-ecmwf-satellite-sea-level-global=climetlab_wekeo_ecmwf.satellite_sea_level_global:satellite_sea_level_global",
            "wekeo-ecmwf-satellite-sea-level-mediterranean=climetlab_wekeo_ecmwf.satellite_sea_level_mediterranean:satellite_sea_level_mediterranean",
            "wekeo-ecmwf-satellite-soil-moisture=climetlab_wekeo_ecmwf.satellite_soil_moisture:satellite_soil_moisture",
            "wekeo-ecmwf-satellite-surface-radiation-budget=climetlab_wekeo_ecmwf.satellite_surface_radiation_budget:satellite_surface_radiation_budget",
            "wekeo-ecmwf-satellite-total-column-water-vapour-land-ocean=climetlab_wekeo_ecmwf.satellite_total_column_water_vapour_land_ocean:satellite_total_column_water_vapour_land_ocean",
            "wekeo-ecmwf-satellite-total-column-water-vapour-ocean=climetlab_wekeo_ecmwf.satellite_total_column_water_vapour_ocean:satellite_total_column_water_vapour_ocean",
            "wekeo-ecmwf-satellite-upper-troposphere-humidity=climetlab_wekeo_ecmwf.satellite_upper_troposphere_humidity:satellite_upper_troposphere_humidity",
            "wekeo-ecmwf-seasonal-monthly-pressure-levels=climetlab_wekeo_ecmwf.seasonal_monthly_pressure_levels:seasonal_monthly_pressure_levels",
            "wekeo-ecmwf-seasonal-monthly-single-levels=climetlab_wekeo_ecmwf.seasonal_monthly_single_levels:seasonal_monthly_single_levels",
            "wekeo-ecmwf-seasonal-original-pressure-levels=climetlab_wekeo_ecmwf.seasonal_original_pressure_levels:seasonal_original_pressure_levels",
            "wekeo-ecmwf-seasonal-original-single-levels=climetlab_wekeo_ecmwf.seasonal_original_single_levels:seasonal_original_single_levels",
            "wekeo-ecmwf-seasonal-postprocessed-pressure-levels=climetlab_wekeo_ecmwf.seasonal_postprocessed_pressure_levels:seasonal_postprocessed_pressure_levels",
            "wekeo-ecmwf-seasonal-postprocessed-single-levels=climetlab_wekeo_ecmwf.seasonal_postprocessed_single_levels:seasonal_postprocessed_single_levels",
            "wekeo-ecmwf-sis-agrometeorological-indicators=climetlab_wekeo_ecmwf.sis_agrometeorological_indicators:sis_agrometeorological_indicators",
            "wekeo-ecmwf-sis-biodiversity-cmip5-global=climetlab_wekeo_ecmwf.sis_biodiversity_cmip5_global:sis_biodiversity_cmip5_global",
            "wekeo-ecmwf-sis-biodiversity-cmip5-regional=climetlab_wekeo_ecmwf.sis_biodiversity_cmip5_regional:sis_biodiversity_cmip5_regional",
            "wekeo-ecmwf-sis-biodiversity-era5-global=climetlab_wekeo_ecmwf.sis_biodiversity_era5_global:sis_biodiversity_era5_global",
            "wekeo-ecmwf-sis-biodiversity-era5-regional=climetlab_wekeo_ecmwf.sis_biodiversity_era5_regional:sis_biodiversity_era5_regional",
            "wekeo-ecmwf-sis-ecv-cmip5-bias-corrected=climetlab_wekeo_ecmwf.sis_ecv_cmip5_bias_corrected:sis_ecv_cmip5_bias_corrected",
            "wekeo-ecmwf-sis-european-risk-extreme-precipitation-indicators=climetlab_wekeo_ecmwf.sis_european_risk_extreme_precipitation_indicators:sis_european_risk_extreme_precipitation_indicators",
            "wekeo-ecmwf-sis-european-risk-flood-indicators=climetlab_wekeo_ecmwf.sis_european_risk_flood_indicators:sis_european_risk_flood_indicators",
            "wekeo-ecmwf-sis-european-wind-storm-indicators=climetlab_wekeo_ecmwf.sis_european_wind_storm_indicators:sis_european_wind_storm_indicators",
            "wekeo-ecmwf-sis-european-wind-storm-synthetic-events=climetlab_wekeo_ecmwf.sis_european_wind_storm_synthetic_events:sis_european_wind_storm_synthetic_events",
            "wekeo-ecmwf-sis-health-vector=climetlab_wekeo_ecmwf.sis_health_vector:sis_health_vector",
            "wekeo-ecmwf-sis-heat-and-cold-spells=climetlab_wekeo_ecmwf.sis_heat_and_cold_spells:sis_heat_and_cold_spells",
            "wekeo-ecmwf-sis-hydrology-meteorology-derived-projections=climetlab_wekeo_ecmwf.sis_hydrology_meteorology_derived_projections:sis_hydrology_meteorology_derived_projections",
            "wekeo-ecmwf-sis-hydrology-variables-derived-projections=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_projections:sis_hydrology_variables_derived_projections",
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-forecast=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_seasonal_forecast:sis_hydrology_variables_derived_seasonal_forecast",
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-reforecast=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_seasonal_reforecast:sis_hydrology_variables_derived_seasonal_reforecast",
            "wekeo-ecmwf-sis-marine-properties=climetlab_wekeo_ecmwf.sis_marine_properties:sis_marine_properties",
            "wekeo-ecmwf-sis-shipping-arctic=climetlab_wekeo_ecmwf.sis_shipping_arctic:sis_shipping_arctic",
            "wekeo-ecmwf-sis-shipping-consumption-on-routes=climetlab_wekeo_ecmwf.sis_shipping_consumption_on_routes:sis_shipping_consumption_on_routes",
            "wekeo-ecmwf-sis-temperature-statistics=climetlab_wekeo_ecmwf.sis_temperature_statistics:sis_temperature_statistics",
            "wekeo-ecmwf-sis-urban-climate-cities=climetlab_wekeo_ecmwf.sis_urban_climate_cities:sis_urban_climate_cities",
            "wekeo-ecmwf-sis-water-hydrological-change=climetlab_wekeo_ecmwf.sis_water_hydrological_change:sis_water_hydrological_change",
            # Other datasets can be included here
            # "climetlab-wekeo-ecmwf-dataset-2= climetlab_wekeo_ecmwf.main2:Main2",  # noqa: E501
        ]
        # source plugins would be here
        # "climetlab.sources": []
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
