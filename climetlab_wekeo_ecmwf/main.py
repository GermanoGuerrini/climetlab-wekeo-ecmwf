#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

import xarray as xr

import climetlab as cml
from climetlab import Dataset

__version__ = "0.1.0"


class Main(Dataset):
    name = None
    home_page = "https://www.wekeo.eu/"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "https://www.copernicus.eu/en/access-data/copyright-and-licences"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://www.copernicus.eu/en/access-data/copyright-and-licence"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    def __init__(self, *args, **kwargs):

        query = {
            "datasetId": f"{self.dataset}",
        }

        choices = dict(zip(self.choices, [kwargs[c] for c in self.choices]))
        if any(c is not None for c in choices.values()):
            query["stringChoiceValues"] = []

            for choice in choices:
                if choices.get(choice) is not None:

                    if choice == "format_":
                        label = "format"
                    else:
                        label = choice

                    query["stringChoiceValues"].append(
                        {"name": label, "value": choices[choice]}
                    )

        string_selects = dict(zip(self.string_selects, [kwargs[v] for v in self.string_selects]))
        if any(v is not None for v in string_selects.values()):
            query["multiStringSelectValues"] = []

            for variable in string_selects:
                if string_selects.get(variable) is not None:

                    if variable == "format_":
                        label = "format"
                    else:
                        label = variable

                    query["multiStringSelectValues"].append(
                        {"name": label, "value": string_selects[variable]}
                    )

        self.source = cml.load_source("wekeo", query)
        self._xarray = None

    def pre_concat(self, datasets):
        """Hook for subclasses."""
        return datasets

    def post_concat(self, datasets, array):
        """Hook for subclasses."""
        return array

    def to_xarray(self, **kwargs):
        if self._xarray is not None:
            return self._xarray

        datasets = [
            xr.open_dataset(s, chunks="auto", engine="netcdf4") for s in self.source.sources
        ]
        datasets = self.pre_concat(datasets)
        array = xr.concat(datasets, dim="time")
        array = self.post_concat(datasets, array)
        self._xarray = array
        return self._xarray