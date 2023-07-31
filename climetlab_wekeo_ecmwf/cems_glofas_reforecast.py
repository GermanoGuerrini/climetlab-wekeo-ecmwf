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


class cems_glofas_reforecast(Main):
    name = "EO:ECMWF:DAT:CEMS_GLOFAS_REFORECAST"
    dataset = "EO:ECMWF:DAT:CEMS_GLOFAS_REFORECAST"

    choices = [
        "format_",
    ]

    string_selects = [
        "system_version",
        "system_version",
        "hydrological_model",
        "product_type",
        "variable",
        "hyear",
        "hmonth",
        "hday",
        "leadtime_hour",
    ]

    @normalize(
        "system_version",
        [
            "version_3_1",
        ],
        multiple=True,
    )
    @normalize(
        "system_version",
        [
            "version_2_2",
        ],
        multiple=True,
    )
    @normalize(
        "hydrological_model",
        [
            "htessel_lisflood",
            "lisflood",
        ],
        multiple=True,
    )
    @normalize(
        "product_type",
        [
            "control_reforecast",
            "ensemble_perturbed_reforecasts",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "river_discharge_in_the_last_24_hours",
        ],
        multiple=True,
    )
    @normalize(
        "hyear",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "hmonth",
        [
            "april",
            "august",
            "december",
            "february",
            "january",
            "july",
            "june",
            "march",
            "may",
            "november",
            "october",
            "september",
        ],
        multiple=True,
    )
    @normalize(
        "hday",
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
        "leadtime_hour",
        [
            "1008",
            "1032",
            "1056",
            "1080",
            "1104",
            "120",
            "144",
            "168",
            "192",
            "216",
            "24",
            "240",
            "264",
            "288",
            "312",
            "336",
            "360",
            "384",
            "408",
            "432",
            "456",
            "48",
            "480",
            "504",
            "528",
            "552",
            "576",
            "600",
            "624",
            "648",
            "672",
            "696",
            "72",
            "720",
            "744",
            "768",
            "792",
            "816",
            "840",
            "864",
            "888",
            "912",
            "936",
            "96",
            "960",
            "984",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf4.zip",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        system_version,
        system_version,
        hydrological_model,
        product_type,
        variable,
        hyear,
        hmonth,
        hday,
        leadtime_hour,
        format_,
        area=None,
    ):
        super().__init__(
            system_version=system_version,
            system_version=system_version,
            hydrological_model=hydrological_model,
            product_type=product_type,
            variable=variable,
            hyear=hyear,
            hmonth=hmonth,
            hday=hday,
            leadtime_hour=leadtime_hour,
            format_=format_,
            area=area,
        )
