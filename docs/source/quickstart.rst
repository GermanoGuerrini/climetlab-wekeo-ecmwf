Quick start
===========

Once the plugin is installed, it can be used directly into a Jupyter notebook.


.. code-block:: python

    import climetlab as cml

    ds = cml.load_dataset("wekeo-ecmwf-reanalysis-era5-single-levels-monthly-means",
        product_type="monthly_averaged_reanalysis_by_hour_of_day",
        month="01",
        year="2019",
        time=[
            "00:00",
            "01:00"
        ],
        variable=[
            "2m_temperature",
            "surface_runoff"
        ],
        format_="netcdf",
    )

    xarr = ds.to_xarray()
    xarr.t2m.isel(time=0).plot()

.. image:: ../images/plot.png
    :width: 400

.. note::
    When `to_xarray` gets called, it tries to combine all the downloaded files, assuming that they can be either
    concatenated by the time dimension or merged if they feature the same time span and non-overlapping variables.
    Therefore, depending on how the data are sliced through files, the default algorith cannot work or make sense.
    In those cases, it is up to the users to determine the best strategy relatively to their needs.