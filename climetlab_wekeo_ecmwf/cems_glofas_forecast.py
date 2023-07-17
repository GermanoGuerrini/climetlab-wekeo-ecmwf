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


class cems_glofas_forecast(Main):
    name = "EO:ECMWF:DAT:CEMS_GLOFAS_FORECAST"
    dataset = "EO:ECMWF:DAT:CEMS_GLOFAS_FORECAST"

    choices = [
        "format_",
    ]

    string_selects = [
        "system_version",
        "system_version",
        "system_version",
        "hydrological_model",
        "product_type",
        "variable",
        "year",
        "month",
        "day",
        "leadtime_hour",
    ]

    @normalize("area", "bounding-box(list)")
    @normalize(
        "system_version",
        [
            "operational",
        ],
        multiple=True,
    )
    @normalize(
        "system_version",
        [
            "version_2_1",
        ],
        multiple=True,
    )
    @normalize(
        "system_version",
        [
            "version_3_1",
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
            "control_forecast",
            "ensemble_perturbed_forecasts",
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
        "year",
        [
            "2019",
            "2020",
            "2021",
            "2022",
            "2023",
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
        "leadtime_hour",
        [
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
            "96",
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
    def __init__(
        self,
        area=None,
        system_version,
        system_version,
        system_version,
        hydrological_model,
        product_type,
        variable,
        year,
        month,
        day,
        leadtime_hour,
        format_,
    ):
        super().__init__(
            area=area,
            system_version=system_version,
            system_version=system_version,
            system_version=system_version,
            hydrological_model=hydrological_model,
            product_type=product_type,
            variable=variable,
            year=year,
            month=month,
            day=day,
            leadtime_hour=leadtime_hour,
            format_=format_,
        )
