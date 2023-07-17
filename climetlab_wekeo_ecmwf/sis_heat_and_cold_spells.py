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


class sis_heat_and_cold_spells(Main):
    name = "EO:ECMWF:DAT:SIS_HEAT_AND_COLD_SPELLS"
    dataset = "EO:ECMWF:DAT:SIS_HEAT_AND_COLD_SPELLS"

    choices = [
        "definition",
        "format_",
    ]

    string_selects = [
        "variable",
        "experiment",
        "ensemble_statistic",
    ]

    @normalize(
        "variable",
        [
            "cold_spell_days",
            "heat_wave_days",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "rcp4_5",
            "rcp8_5",
        ],
        multiple=True,
    )
    @normalize(
        "ensemble_statistic",
        [
            "ensemble_members_average",
            "ensemble_members_standard_deviation",
        ],
        multiple=True,
    )
    @normalize(
        "definition",
        [
            "climatological_related",
            "country_related",
            "health_related",
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
        variable,
        experiment,
        ensemble_statistic,
        definition,
        format_,
    ):
        super().__init__(
            variable=variable,
            experiment=experiment,
            ensemble_statistic=ensemble_statistic,
            definition=definition,
            format_=format_,
        )
