#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_ecmwf.main import Main


class sis_hydrology_meteorology_derived_projections(Main):
    name = "EO:ECMWF:DAT:SIS_HYDROLOGY_METEOROLOGY_DERIVED_PROJECTIONS"
    dataset = "EO:ECMWF:DAT:SIS_HYDROLOGY_METEOROLOGY_DERIVED_PROJECTIONS"

    choices = [
        "product_type",
        "processing_type",
        "variable_type",
        "horizontal_resolution",
        "rcm",
        "gcm",
        "format_",
    ]

    string_selects = [
        "ensemble_member",
        "experiment",
        "period",
        "time_aggregation",
        "variable",
    ]

    @normalize(
        "ensemble_member",
        [
            "r12i1p1",
            "r1i1p1",
            "r2i1p1",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "degree_scenario",
            "historical",
            "rcp_2_6",
            "rcp_4_5",
            "rcp_8_5",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "1970",
            "1971",
            "1971_2000",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "1_5_c",
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2011_2040",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
            "2024",
            "2025",
            "2026",
            "2027",
            "2028",
            "2029",
            "2030",
            "2031",
            "2032",
            "2033",
            "2034",
            "2035",
            "2036",
            "2037",
            "2038",
            "2039",
            "2040",
            "2041",
            "2041_2070",
            "2042",
            "2043",
            "2044",
            "2045",
            "2046",
            "2047",
            "2048",
            "2049",
            "2050",
            "2051",
            "2052",
            "2053",
            "2054",
            "2055",
            "2056",
            "2057",
            "2058",
            "2059",
            "2060",
            "2061",
            "2062",
            "2063",
            "2064",
            "2065",
            "2066",
            "2067",
            "2068",
            "2069",
            "2070",
            "2071",
            "2071_2100",
            "2072",
            "2073",
            "2074",
            "2075",
            "2076",
            "2077",
            "2078",
            "2079",
            "2080",
            "2081",
            "2082",
            "2083",
            "2084",
            "2085",
            "2086",
            "2087",
            "2088",
            "2089",
            "2090",
            "2091",
            "2092",
            "2093",
            "2094",
            "2095",
            "2096",
            "2097",
            "2098",
            "2099",
            "2100",
            "2_0_c",
            "3_0_c",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "annual_mean",
            "daily",
            "monthly_mean",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "2m_air_temperature",
            "highest_5_day_precipitation_amount",
            "longest_dry_spells",
            "number_of_dry_spells",
            "precipitation",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "climate_impact_indicators",
            "essential_climate_variables",
        ],
    )
    @normalize(
        "processing_type",
        [
            "bias_corrected",
            "original",
        ],
    )
    @normalize(
        "variable_type",
        [
            "absolute_change_from_reference_period",
            "absolute_values",
            "relative_change_from_reference_period",
        ],
    )
    @normalize(
        "horizontal_resolution",
        [
            "0_11_degrees",
            "5_km",
        ],
    )
    @normalize(
        "rcm",
        [
            "cclm4_8_17",
            "csc_remo2009",
            "racmo22e",
            "rca4",
        ],
    )
    @normalize(
        "gcm",
        [
            "ec_earth",
            "hadgem2_es",
            "mpi_esm_lr",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        ensemble_member,
        experiment,
        period,
        time_aggregation,
        variable,
        product_type,
        processing_type,
        variable_type,
        horizontal_resolution,
        rcm,
        gcm,
        format_,
    ):
        super().__init__(
            ensemble_member=ensemble_member,
            experiment=experiment,
            period=period,
            time_aggregation=time_aggregation,
            variable=variable,
            product_type=product_type,
            processing_type=processing_type,
            variable_type=variable_type,
            horizontal_resolution=horizontal_resolution,
            rcm=rcm,
            gcm=gcm,
            format_=format_,
        )
