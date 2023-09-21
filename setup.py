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
            "wekeo-ecmwf-cems-fire-historical-v1=climetlab_wekeo_ecmwf.cems_fire_historical_v1:cems_fire_historical_v1",
            "wekeo-ecmwf-derived-near-surface-meteorological-variables=climetlab_wekeo_ecmwf.derived_near_surface_meteorological_variables:derived_near_surface_meteorological_variables",
            "wekeo-ecmwf-derived-reanalysis-energy-moisture-budget=climetlab_wekeo_ecmwf.derived_reanalysis_energy_moisture_budget:derived_reanalysis_energy_moisture_budget",
            "wekeo-ecmwf-derived-utci-historical=climetlab_wekeo_ecmwf.derived_utci_historical:derived_utci_historical",
            "wekeo-ecmwf-ecv-for-climate-change=climetlab_wekeo_ecmwf.ecv_for_climate_change:ecv_for_climate_change",
            "wekeo-ecmwf-efas-forecast=climetlab_wekeo_ecmwf.efas_forecast:efas_forecast",
            "wekeo-ecmwf-efas-historical=climetlab_wekeo_ecmwf.efas_historical:efas_historical",
            "wekeo-ecmwf-efas-reforecast=climetlab_wekeo_ecmwf.efas_reforecast:efas_reforecast",
            "wekeo-ecmwf-efas-seasonal-reforecast=climetlab_wekeo_ecmwf.efas_seasonal_reforecast:efas_seasonal_reforecast",
            "wekeo-ecmwf-efas-seasonal=climetlab_wekeo_ecmwf.efas_seasonal:efas_seasonal",
            "wekeo-ecmwf-insitu-glaciers-elevation-mass=climetlab_wekeo_ecmwf.insitu_glaciers_elevation_mass:insitu_glaciers_elevation_mass",
            "wekeo-ecmwf-insitu-glaciers-extent=climetlab_wekeo_ecmwf.insitu_glaciers_extent:insitu_glaciers_extent",
            "wekeo-ecmwf-insitu-gridded-observations-alpine-precipitation=climetlab_wekeo_ecmwf.insitu_gridded_observations_alpine_precipitation:insitu_gridded_observations_alpine_precipitation",
            "wekeo-ecmwf-insitu-gridded-observations-europe=climetlab_wekeo_ecmwf.insitu_gridded_observations_europe:insitu_gridded_observations_europe",
            "wekeo-ecmwf-insitu-gridded-observations-global-and-regional=climetlab_wekeo_ecmwf.insitu_gridded_observations_global_and_regional:insitu_gridded_observations_global_and_regional",
            "wekeo-ecmwf-insitu-gridded-observations-nordic=climetlab_wekeo_ecmwf.insitu_gridded_observations_nordic:insitu_gridded_observations_nordic",
            "wekeo-ecmwf-insitu-observations-gnss=climetlab_wekeo_ecmwf.insitu_observations_gnss:insitu_observations_gnss",
            "wekeo-ecmwf-insitu-observations-gruan-reference-network=climetlab_wekeo_ecmwf.insitu_observations_gruan_reference_network:insitu_observations_gruan_reference_network",
            "wekeo-ecmwf-insitu-observations-igra-baseline-network=climetlab_wekeo_ecmwf.insitu_observations_igra_baseline_network:insitu_observations_igra_baseline_network",
            "wekeo-ecmwf-insitu-observations-surface-land=climetlab_wekeo_ecmwf.insitu_observations_surface_land:insitu_observations_surface_land",
            "wekeo-ecmwf-insitu-observations-surface-marine=climetlab_wekeo_ecmwf.insitu_observations_surface_marine:insitu_observations_surface_marine",
            "wekeo-ecmwf-insitu-observations-woudc-ozone-total-column-and-profiles=climetlab_wekeo_ecmwf.insitu_observations_woudc_ozone_total_column_and_profiles:insitu_observations_woudc_ozone_total_column_and_profiles",
            "wekeo-ecmwf-projections-cmip5-daily-pressure-levels=climetlab_wekeo_ecmwf.projections_cmip5_daily_pressure_levels:projections_cmip5_daily_pressure_levels",
            "wekeo-ecmwf-projections-cmip5-daily-single-levels=climetlab_wekeo_ecmwf.projections_cmip5_daily_single_levels:projections_cmip5_daily_single_levels",
            "wekeo-ecmwf-projections-cmip5-monthly-pressure-levels=climetlab_wekeo_ecmwf.projections_cmip5_monthly_pressure_levels:projections_cmip5_monthly_pressure_levels",
            "wekeo-ecmwf-projections-cmip5-monthly-single-levels=climetlab_wekeo_ecmwf.projections_cmip5_monthly_single_levels:projections_cmip5_monthly_single_levels",
            "wekeo-ecmwf-projections-cmip6=climetlab_wekeo_ecmwf.projections_cmip6:projections_cmip6",
            "wekeo-ecmwf-projections-cordex-domains-single-levels=climetlab_wekeo_ecmwf.projections_cordex_domains_single_levels:projections_cordex_domains_single_levels",
            "wekeo-ecmwf-reanalysis-carra-height-levels=climetlab_wekeo_ecmwf.reanalysis_carra_height_levels:reanalysis_carra_height_levels",
            "wekeo-ecmwf-reanalysis-carra-model-levels=climetlab_wekeo_ecmwf.reanalysis_carra_model_levels:reanalysis_carra_model_levels",
            "wekeo-ecmwf-reanalysis-carra-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_carra_pressure_levels:reanalysis_carra_pressure_levels",
            "wekeo-ecmwf-reanalysis-carra-single-levels=climetlab_wekeo_ecmwf.reanalysis_carra_single_levels:reanalysis_carra_single_levels",
            "wekeo-ecmwf-reanalysis-cerra-height-levels=climetlab_wekeo_ecmwf.reanalysis_cerra_height_levels:reanalysis_cerra_height_levels",
            "wekeo-ecmwf-reanalysis-cerra-land=climetlab_wekeo_ecmwf.reanalysis_cerra_land:reanalysis_cerra_land",
            "wekeo-ecmwf-reanalysis-cerra-model-levels=climetlab_wekeo_ecmwf.reanalysis_cerra_model_levels:reanalysis_cerra_model_levels",
            "wekeo-ecmwf-reanalysis-cerra-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_cerra_pressure_levels:reanalysis_cerra_pressure_levels",
            "wekeo-ecmwf-reanalysis-cerra-single-levels=climetlab_wekeo_ecmwf.reanalysis_cerra_single_levels:reanalysis_cerra_single_levels",
            "wekeo-ecmwf-reanalysis-era5-land-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_land_monthly_means:reanalysis_era5_land_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-land=climetlab_wekeo_ecmwf.reanalysis_era5_land:reanalysis_era5_land",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels_monthly_means:reanalysis_era5_pressure_levels_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_era5_pressure_levels:reanalysis_era5_pressure_levels",
            "wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels_monthly_means:reanalysis_era5_single_levels_monthly_means",
            "wekeo-ecmwf-reanalysis-era5-single-levels=climetlab_wekeo_ecmwf.reanalysis_era5_single_levels:reanalysis_era5_single_levels",
            "wekeo-ecmwf-reanalysis-oras5=climetlab_wekeo_ecmwf.reanalysis_oras5:reanalysis_oras5",
            "wekeo-ecmwf-reanalysis-uerra-europe-height-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_height_levels:reanalysis_uerra_europe_height_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-pressure-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_pressure_levels:reanalysis_uerra_europe_pressure_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-single-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_single_levels:reanalysis_uerra_europe_single_levels",
            "wekeo-ecmwf-reanalysis-uerra-europe-soil-levels=climetlab_wekeo_ecmwf.reanalysis_uerra_europe_soil_levels:reanalysis_uerra_europe_soil_levels",
            "wekeo-ecmwf-satellite-aerosol-properties=climetlab_wekeo_ecmwf.satellite_aerosol_properties:satellite_aerosol_properties",
            "wekeo-ecmwf-satellite-albedo=climetlab_wekeo_ecmwf.satellite_albedo:satellite_albedo",
            "wekeo-ecmwf-satellite-carbon-dioxide=climetlab_wekeo_ecmwf.satellite_carbon_dioxide:satellite_carbon_dioxide",
            "wekeo-ecmwf-satellite-cloud-properties=climetlab_wekeo_ecmwf.satellite_cloud_properties:satellite_cloud_properties",
            "wekeo-ecmwf-satellite-earth-radiation-budget=climetlab_wekeo_ecmwf.satellite_earth_radiation_budget:satellite_earth_radiation_budget",
            "wekeo-ecmwf-satellite-fire-burned-area=climetlab_wekeo_ecmwf.satellite_fire_burned_area:satellite_fire_burned_area",
            "wekeo-ecmwf-satellite-fire-radiative-power=climetlab_wekeo_ecmwf.satellite_fire_radiative_power:satellite_fire_radiative_power",
            "wekeo-ecmwf-satellite-greenland-ice-sheet-velocity=climetlab_wekeo_ecmwf.satellite_greenland_ice_sheet_velocity:satellite_greenland_ice_sheet_velocity",
            "wekeo-ecmwf-satellite-humidity-profiles=climetlab_wekeo_ecmwf.satellite_humidity_profiles:satellite_humidity_profiles",
            "wekeo-ecmwf-satellite-ice-sheet-elevation-change=climetlab_wekeo_ecmwf.satellite_ice_sheet_elevation_change:satellite_ice_sheet_elevation_change",
            "wekeo-ecmwf-satellite-ice-sheet-mass-balance=climetlab_wekeo_ecmwf.satellite_ice_sheet_mass_balance:satellite_ice_sheet_mass_balance",
            "wekeo-ecmwf-satellite-lai-fapar=climetlab_wekeo_ecmwf.satellite_lai_fapar:satellite_lai_fapar",
            "wekeo-ecmwf-satellite-lake-water-level=climetlab_wekeo_ecmwf.satellite_lake_water_level:satellite_lake_water_level",
            "wekeo-ecmwf-satellite-lake-water-temperature=climetlab_wekeo_ecmwf.satellite_lake_water_temperature:satellite_lake_water_temperature",
            "wekeo-ecmwf-satellite-land-cover=climetlab_wekeo_ecmwf.satellite_land_cover:satellite_land_cover",
            "wekeo-ecmwf-satellite-methane=climetlab_wekeo_ecmwf.satellite_methane:satellite_methane",
            "wekeo-ecmwf-satellite-ocean-colour=climetlab_wekeo_ecmwf.satellite_ocean_colour:satellite_ocean_colour",
            "wekeo-ecmwf-satellite-ozone-v1=climetlab_wekeo_ecmwf.satellite_ozone_v1:satellite_ozone_v1",
            "wekeo-ecmwf-satellite-precipitation-microwave=climetlab_wekeo_ecmwf.satellite_precipitation_microwave:satellite_precipitation_microwave",
            "wekeo-ecmwf-satellite-precipitation=climetlab_wekeo_ecmwf.satellite_precipitation:satellite_precipitation",
            "wekeo-ecmwf-satellite-sea-ice-concentration=climetlab_wekeo_ecmwf.satellite_sea_ice_concentration:satellite_sea_ice_concentration",
            "wekeo-ecmwf-satellite-sea-ice-edge-type=climetlab_wekeo_ecmwf.satellite_sea_ice_edge_type:satellite_sea_ice_edge_type",
            "wekeo-ecmwf-satellite-sea-ice-thickness=climetlab_wekeo_ecmwf.satellite_sea_ice_thickness:satellite_sea_ice_thickness",
            "wekeo-ecmwf-satellite-sea-level-black-sea=climetlab_wekeo_ecmwf.satellite_sea_level_black_sea:satellite_sea_level_black_sea",
            "wekeo-ecmwf-satellite-sea-level-global=climetlab_wekeo_ecmwf.satellite_sea_level_global:satellite_sea_level_global",
            "wekeo-ecmwf-satellite-sea-level-mediterranean=climetlab_wekeo_ecmwf.satellite_sea_level_mediterranean:satellite_sea_level_mediterranean",
            "wekeo-ecmwf-satellite-sea-surface-temperature-ensemble-product=climetlab_wekeo_ecmwf.satellite_sea_surface_temperature_ensemble_product:satellite_sea_surface_temperature_ensemble_product",
            "wekeo-ecmwf-satellite-sea-surface-temperature=climetlab_wekeo_ecmwf.satellite_sea_surface_temperature:satellite_sea_surface_temperature",
            "wekeo-ecmwf-satellite-soil-moisture=climetlab_wekeo_ecmwf.satellite_soil_moisture:satellite_soil_moisture",
            "wekeo-ecmwf-satellite-surface-radiation-budget=climetlab_wekeo_ecmwf.satellite_surface_radiation_budget:satellite_surface_radiation_budget",
            "wekeo-ecmwf-satellite-total-column-water-vapour-land-ocean=climetlab_wekeo_ecmwf.satellite_total_column_water_vapour_land_ocean:satellite_total_column_water_vapour_land_ocean",
            "wekeo-ecmwf-satellite-total-column-water-vapour-ocean=climetlab_wekeo_ecmwf.satellite_total_column_water_vapour_ocean:satellite_total_column_water_vapour_ocean",
            "wekeo-ecmwf-satellite-upper-troposphere-humidity=climetlab_wekeo_ecmwf.satellite_upper_troposphere_humidity:satellite_upper_troposphere_humidity",
            "wekeo-ecmwf-seasonal-monthly-ocean=climetlab_wekeo_ecmwf.seasonal_monthly_ocean:seasonal_monthly_ocean",
            "wekeo-ecmwf-seasonal-monthly-pressure-levels=climetlab_wekeo_ecmwf.seasonal_monthly_pressure_levels:seasonal_monthly_pressure_levels",
            "wekeo-ecmwf-seasonal-monthly-single-levels=climetlab_wekeo_ecmwf.seasonal_monthly_single_levels:seasonal_monthly_single_levels",
            "wekeo-ecmwf-seasonal-original-pressure-levels=climetlab_wekeo_ecmwf.seasonal_original_pressure_levels:seasonal_original_pressure_levels",
            "wekeo-ecmwf-seasonal-original-single-levels=climetlab_wekeo_ecmwf.seasonal_original_single_levels:seasonal_original_single_levels",
            "wekeo-ecmwf-seasonal-postprocessed-pressure-levels=climetlab_wekeo_ecmwf.seasonal_postprocessed_pressure_levels:seasonal_postprocessed_pressure_levels",
            "wekeo-ecmwf-seasonal-postprocessed-single-levels=climetlab_wekeo_ecmwf.seasonal_postprocessed_single_levels:seasonal_postprocessed_single_levels",
            "wekeo-ecmwf-sis-agroclimatic-indicators=climetlab_wekeo_ecmwf.sis_agroclimatic_indicators:sis_agroclimatic_indicators",
            "wekeo-ecmwf-sis-agrometeorological-indicators=climetlab_wekeo_ecmwf.sis_agrometeorological_indicators:sis_agrometeorological_indicators",
            "wekeo-ecmwf-sis-agroproductivity-indicators=climetlab_wekeo_ecmwf.sis_agroproductivity_indicators:sis_agroproductivity_indicators",
            "wekeo-ecmwf-sis-biodiversity-cmip5-global=climetlab_wekeo_ecmwf.sis_biodiversity_cmip5_global:sis_biodiversity_cmip5_global",
            "wekeo-ecmwf-sis-biodiversity-cmip5-regional=climetlab_wekeo_ecmwf.sis_biodiversity_cmip5_regional:sis_biodiversity_cmip5_regional",
            "wekeo-ecmwf-sis-biodiversity-era5-global=climetlab_wekeo_ecmwf.sis_biodiversity_era5_global:sis_biodiversity_era5_global",
            "wekeo-ecmwf-sis-biodiversity-era5-regional=climetlab_wekeo_ecmwf.sis_biodiversity_era5_regional:sis_biodiversity_era5_regional",
            "wekeo-ecmwf-sis-ecv-cmip5-bias-corrected=climetlab_wekeo_ecmwf.sis_ecv_cmip5_bias_corrected:sis_ecv_cmip5_bias_corrected",
            "wekeo-ecmwf-sis-energy-derived-projections=climetlab_wekeo_ecmwf.sis_energy_derived_projections:sis_energy_derived_projections",
            "wekeo-ecmwf-sis-energy-derived-reanalysis=climetlab_wekeo_ecmwf.sis_energy_derived_reanalysis:sis_energy_derived_reanalysis",
            "wekeo-ecmwf-sis-european-risk-extreme-precipitation-indicators=climetlab_wekeo_ecmwf.sis_european_risk_extreme_precipitation_indicators:sis_european_risk_extreme_precipitation_indicators",
            "wekeo-ecmwf-sis-european-risk-flood-indicators=climetlab_wekeo_ecmwf.sis_european_risk_flood_indicators:sis_european_risk_flood_indicators",
            "wekeo-ecmwf-sis-european-wind-storm-indicators=climetlab_wekeo_ecmwf.sis_european_wind_storm_indicators:sis_european_wind_storm_indicators",
            "wekeo-ecmwf-sis-european-wind-storm-synthetic-events=climetlab_wekeo_ecmwf.sis_european_wind_storm_synthetic_events:sis_european_wind_storm_synthetic_events",
            "wekeo-ecmwf-sis-extreme-indices-cmip6=climetlab_wekeo_ecmwf.sis_extreme_indices_cmip6:sis_extreme_indices_cmip6",
            "wekeo-ecmwf-sis-fisheries-abundance=climetlab_wekeo_ecmwf.sis_fisheries_abundance:sis_fisheries_abundance",
            "wekeo-ecmwf-sis-fisheries-eutrophication=climetlab_wekeo_ecmwf.sis_fisheries_eutrophication:sis_fisheries_eutrophication",
            "wekeo-ecmwf-sis-fisheries-ocean-fronts=climetlab_wekeo_ecmwf.sis_fisheries_ocean_fronts:sis_fisheries_ocean_fronts",
            "wekeo-ecmwf-sis-health-vector=climetlab_wekeo_ecmwf.sis_health_vector:sis_health_vector",
            "wekeo-ecmwf-sis-heat-and-cold-spells=climetlab_wekeo_ecmwf.sis_heat_and_cold_spells:sis_heat_and_cold_spells",
            "wekeo-ecmwf-sis-hydrology-meteorology-derived-projections=climetlab_wekeo_ecmwf.sis_hydrology_meteorology_derived_projections:sis_hydrology_meteorology_derived_projections",
            "wekeo-ecmwf-sis-hydrology-variables-derived-projections=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_projections:sis_hydrology_variables_derived_projections",
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-forecast=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_seasonal_forecast:sis_hydrology_variables_derived_seasonal_forecast",
            "wekeo-ecmwf-sis-hydrology-variables-derived-seasonal-reforecast=climetlab_wekeo_ecmwf.sis_hydrology_variables_derived_seasonal_reforecast:sis_hydrology_variables_derived_seasonal_reforecast",
            "wekeo-ecmwf-sis-marine-properties=climetlab_wekeo_ecmwf.sis_marine_properties:sis_marine_properties",
            "wekeo-ecmwf-sis-ocean-wave-indicators=climetlab_wekeo_ecmwf.sis_ocean_wave_indicators:sis_ocean_wave_indicators",
            "wekeo-ecmwf-sis-ocean-wave-timeseries=climetlab_wekeo_ecmwf.sis_ocean_wave_timeseries:sis_ocean_wave_timeseries",
            "wekeo-ecmwf-sis-offshore-windfarm-indicators=climetlab_wekeo_ecmwf.sis_offshore_windfarm_indicators:sis_offshore_windfarm_indicators",
            "wekeo-ecmwf-sis-shipping-arctic=climetlab_wekeo_ecmwf.sis_shipping_arctic:sis_shipping_arctic",
            "wekeo-ecmwf-sis-shipping-consumption-on-routes=climetlab_wekeo_ecmwf.sis_shipping_consumption_on_routes:sis_shipping_consumption_on_routes",
            "wekeo-ecmwf-sis-soil-erosion=climetlab_wekeo_ecmwf.sis_soil_erosion:sis_soil_erosion",
            "wekeo-ecmwf-sis-temperature-statistics=climetlab_wekeo_ecmwf.sis_temperature_statistics:sis_temperature_statistics",
            "wekeo-ecmwf-sis-tourism-climate-suitability-indicators=climetlab_wekeo_ecmwf.sis_tourism_climate_suitability_indicators:sis_tourism_climate_suitability_indicators",
            "wekeo-ecmwf-sis-tourism-fire-danger-indicators=climetlab_wekeo_ecmwf.sis_tourism_fire_danger_indicators:sis_tourism_fire_danger_indicators",
            "wekeo-ecmwf-sis-tourism-snow-indicators=climetlab_wekeo_ecmwf.sis_tourism_snow_indicators:sis_tourism_snow_indicators",
            "wekeo-ecmwf-sis-urban-climate-cities=climetlab_wekeo_ecmwf.sis_urban_climate_cities:sis_urban_climate_cities",
            "wekeo-ecmwf-sis-water-hydrological-change=climetlab_wekeo_ecmwf.sis_water_hydrological_change:sis_water_hydrological_change",
            "wekeo-ecmwf-sis-water-level-change-indicators-cmip6=climetlab_wekeo_ecmwf.sis_water_level_change_indicators_cmip6:sis_water_level_change_indicators_cmip6",
            "wekeo-ecmwf-sis-water-level-change-indicators=climetlab_wekeo_ecmwf.sis_water_level_change_indicators:sis_water_level_change_indicators",
            "wekeo-ecmwf-sis-water-level-change-timeseries-cmip6=climetlab_wekeo_ecmwf.sis_water_level_change_timeseries_cmip6:sis_water_level_change_timeseries_cmip6",
            "wekeo-ecmwf-sis-water-level-change-timeseries=climetlab_wekeo_ecmwf.sis_water_level_change_timeseries:sis_water_level_change_timeseries",
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
