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


class insitu_glaciers_elevation_mass(Main):
    name = "EO:ECMWF:DAT:INSITU_GLACIERS_ELEVATION_MASS"
    dataset = "EO:ECMWF:DAT:INSITU_GLACIERS_ELEVATION_MASS"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "product_type",
        "file_version",
    ]

    @normalize(
        "product_type",
        [
            "elevation_change",
            "mass_balance",
        ],
        multiple=True,
    )
    @normalize(
        "file_version",
        [
            "20170405",
            "20171004",
            "20180601",
            "20181103",
            "20191202",
            "20200824",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all",
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
        product_type,
        file_version,
        variable="all",
        format_,
    ):
        super().__init__(
            product_type=product_type,
            file_version=file_version,
            variable=variable,
            format_=format_,
        )
