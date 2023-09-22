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


class insitu_observations_woudc_ozone_total_column_and_profiles(Main):
    name = "EO:ECMWF:DAT:INSITU_OBSERVATIONS_WOUDC_OZONE_TOTAL_COLUMN_AND_PROFILES"
    dataset = "EO:ECMWF:DAT:INSITU_OBSERVATIONS_WOUDC_OZONE_TOTAL_COLUMN_AND_PROFILES"

    choices = [
        "observation_type",
        "year",
        "format_",
    ]

    string_selects = [
        "day",
        "month",
        "variable",
    ]

    @normalize("area", "bounding-box(list)")
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
        "variable",
        [
            "air_temperature",
            "column_sulphur_dioxide",
            "geopotential_height",
            "ozone_partial_pressure",
            "relative_humidity",
            "total_ozone_column",
            "total_ozone_column_standard_deviation",
            "wind_from_direction",
            "wind_speed",
        ],
        multiple=True,
    )
    @normalize(
        "observation_type",
        [
            "total_column",
            "vertical_profile",
        ],
    )
    @normalize(
        "year",
        [
            "1924",
            "1925",
            "1926",
            "1927",
            "1928",
            "1929",
            "1930",
            "1931",
            "1932",
            "1933",
            "1934",
            "1935",
            "1936",
            "1937",
            "1938",
            "1939",
            "1940",
            "1941",
            "1942",
            "1943",
            "1944",
            "1945",
            "1946",
            "1947",
            "1948",
            "1949",
            "1950",
            "1951",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
            "1958",
            "1959",
            "1960",
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
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
    )
    @normalize(
        "format_",
        [
            "csv-lev.zip",
            "csv-obs.zip",
        ],
    )
    def __init__(
        self,
        area=None,
        day=None,
        month=None,
        variable=None,
        observation_type=None,
        year=None,
        format_=None,
    ):
        super().__init__(
            area=area,
            day=day,
            month=month,
            variable=variable,
            observation_type=observation_type,
            year=year,
            format_=format_,
        )
