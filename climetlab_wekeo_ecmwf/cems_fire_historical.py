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


class cems_fire_historical(Main):
    name = "EO:ECMWF:DAT:CEMS_FIRE_HISTORICAL"
    dataset = "EO:ECMWF:DAT:CEMS_FIRE_HISTORICAL"

    choices = [
        "format_",
    ]

    string_selects = [
        "product_type",
        "variable",
        "version",
        "year",
        "month",
        "day",
        "dataset",
    ]

    @normalize(
        "dataset",
        [
            "Consolidated dataset",
            "Intermediate dataset",
        ],
        multiple=True,
    )
    @normalize(
        "day",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "ensemble_mean",
            "ensemble_members",
            "ensemble_spread",
            "reanalysis",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "build_up_index",
            "burning_index",
            "danger_risk",
            "drought_code",
            "duff_moisture_code",
            "energy_release_component",
            "fine_fuel_moisture_code",
            "fire_daily_severity_rating",
            "fire_danger_index",
            "fire_weather_index",
            "ignition_component",
            "initial_fire_spread_index",
            "keetch_byram_drought_index",
            "spread_component",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "3.0",
            "3.1",
            "4.0",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        ],
        multiple=True,
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
        dataset,
        day,
        month,
        product_type,
        variable,
        version,
        year,
        format_,
    ):
        super().__init__(
            dataset=dataset,
            day=day,
            month=month,
            product_type=product_type,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
        )
