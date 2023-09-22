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


class seasonal_original_single_levels(Main):
    name = "EO:ECMWF:DAT:SEASONAL_ORIGINAL_SINGLE_LEVELS"
    dataset = "EO:ECMWF:DAT:SEASONAL_ORIGINAL_SINGLE_LEVELS"

    choices = [
        "originating_centre",
        "system",
        "format_",
    ]

    string_selects = [
        "day",
        "leadtime_hour",
        "month",
        "variable",
        "year",
    ]

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
            "0",
            "1002",
            "1008",
            "1014",
            "102",
            "1020",
            "1026",
            "1032",
            "1038",
            "1044",
            "1050",
            "1056",
            "1062",
            "1068",
            "1074",
            "108",
            "1080",
            "1086",
            "1092",
            "1098",
            "1104",
            "1110",
            "1116",
            "1122",
            "1128",
            "1134",
            "114",
            "1140",
            "1146",
            "1152",
            "1158",
            "1164",
            "1170",
            "1176",
            "1182",
            "1188",
            "1194",
            "12",
            "120",
            "1200",
            "1206",
            "1212",
            "1218",
            "1224",
            "1230",
            "1236",
            "1242",
            "1248",
            "1254",
            "126",
            "1260",
            "1266",
            "1272",
            "1278",
            "1284",
            "1290",
            "1296",
            "1302",
            "1308",
            "1314",
            "132",
            "1320",
            "1326",
            "1332",
            "1338",
            "1344",
            "1350",
            "1356",
            "1362",
            "1368",
            "1374",
            "138",
            "1380",
            "1386",
            "1392",
            "1398",
            "1404",
            "1410",
            "1416",
            "1422",
            "1428",
            "1434",
            "144",
            "1440",
            "1446",
            "1452",
            "1458",
            "1464",
            "1470",
            "1476",
            "1482",
            "1488",
            "1494",
            "150",
            "1500",
            "1506",
            "1512",
            "1518",
            "1524",
            "1530",
            "1536",
            "1542",
            "1548",
            "1554",
            "156",
            "1560",
            "1566",
            "1572",
            "1578",
            "1584",
            "1590",
            "1596",
            "1602",
            "1608",
            "1614",
            "162",
            "1620",
            "1626",
            "1632",
            "1638",
            "1644",
            "1650",
            "1656",
            "1662",
            "1668",
            "1674",
            "168",
            "1680",
            "1686",
            "1692",
            "1698",
            "1704",
            "1710",
            "1716",
            "1722",
            "1728",
            "1734",
            "174",
            "1740",
            "1746",
            "1752",
            "1758",
            "1764",
            "1770",
            "1776",
            "1782",
            "1788",
            "1794",
            "18",
            "180",
            "1800",
            "1806",
            "1812",
            "1818",
            "1824",
            "1830",
            "1836",
            "1842",
            "1848",
            "1854",
            "186",
            "1860",
            "1866",
            "1872",
            "1878",
            "1884",
            "1890",
            "1896",
            "1902",
            "1908",
            "1914",
            "192",
            "1920",
            "1926",
            "1932",
            "1938",
            "1944",
            "1950",
            "1956",
            "1962",
            "1968",
            "1974",
            "198",
            "1980",
            "1986",
            "1992",
            "1998",
            "2004",
            "2010",
            "2016",
            "2022",
            "2028",
            "2034",
            "204",
            "2040",
            "2046",
            "2052",
            "2058",
            "2064",
            "2070",
            "2076",
            "2082",
            "2088",
            "2094",
            "210",
            "2100",
            "2106",
            "2112",
            "2118",
            "2124",
            "2130",
            "2136",
            "2142",
            "2148",
            "2154",
            "216",
            "2160",
            "2166",
            "2172",
            "2178",
            "2184",
            "2190",
            "2196",
            "2202",
            "2208",
            "2214",
            "222",
            "2220",
            "2226",
            "2232",
            "2238",
            "2244",
            "2250",
            "2256",
            "2262",
            "2268",
            "2274",
            "228",
            "2280",
            "2286",
            "2292",
            "2298",
            "2304",
            "2310",
            "2316",
            "2322",
            "2328",
            "2334",
            "234",
            "2340",
            "2346",
            "2352",
            "2358",
            "2364",
            "2370",
            "2376",
            "2382",
            "2388",
            "2394",
            "24",
            "240",
            "2400",
            "2406",
            "2412",
            "2418",
            "2424",
            "2430",
            "2436",
            "2442",
            "2448",
            "2454",
            "246",
            "2460",
            "2466",
            "2472",
            "2478",
            "2484",
            "2490",
            "2496",
            "2502",
            "2508",
            "2514",
            "252",
            "2520",
            "2526",
            "2532",
            "2538",
            "2544",
            "2550",
            "2556",
            "2562",
            "2568",
            "2574",
            "258",
            "2580",
            "2586",
            "2592",
            "2598",
            "2604",
            "2610",
            "2616",
            "2622",
            "2628",
            "2634",
            "264",
            "2640",
            "2646",
            "2652",
            "2658",
            "2664",
            "2670",
            "2676",
            "2682",
            "2688",
            "2694",
            "270",
            "2700",
            "2706",
            "2712",
            "2718",
            "2724",
            "2730",
            "2736",
            "2742",
            "2748",
            "2754",
            "276",
            "2760",
            "2766",
            "2772",
            "2778",
            "2784",
            "2790",
            "2796",
            "2802",
            "2808",
            "2814",
            "282",
            "2820",
            "2826",
            "2832",
            "2838",
            "2844",
            "2850",
            "2856",
            "2862",
            "2868",
            "2874",
            "288",
            "2880",
            "2886",
            "2892",
            "2898",
            "2904",
            "2910",
            "2916",
            "2922",
            "2928",
            "2934",
            "294",
            "2940",
            "2946",
            "2952",
            "2958",
            "2964",
            "2970",
            "2976",
            "2982",
            "2988",
            "2994",
            "30",
            "300",
            "3000",
            "3006",
            "3012",
            "3018",
            "3024",
            "3030",
            "3036",
            "3042",
            "3048",
            "3054",
            "306",
            "3060",
            "3066",
            "3072",
            "3078",
            "3084",
            "3090",
            "3096",
            "3102",
            "3108",
            "3114",
            "312",
            "3120",
            "3126",
            "3132",
            "3138",
            "3144",
            "3150",
            "3156",
            "3162",
            "3168",
            "3174",
            "318",
            "3180",
            "3186",
            "3192",
            "3198",
            "3204",
            "3210",
            "3216",
            "3222",
            "3228",
            "3234",
            "324",
            "3240",
            "3246",
            "3252",
            "3258",
            "3264",
            "3270",
            "3276",
            "3282",
            "3288",
            "3294",
            "330",
            "3300",
            "3306",
            "3312",
            "3318",
            "3324",
            "3330",
            "3336",
            "3342",
            "3348",
            "3354",
            "336",
            "3360",
            "3366",
            "3372",
            "3378",
            "3384",
            "3390",
            "3396",
            "3402",
            "3408",
            "3414",
            "342",
            "3420",
            "3426",
            "3432",
            "3438",
            "3444",
            "3450",
            "3456",
            "3462",
            "3468",
            "3474",
            "348",
            "3480",
            "3486",
            "3492",
            "3498",
            "3504",
            "3510",
            "3516",
            "3522",
            "3528",
            "3534",
            "354",
            "3540",
            "3546",
            "3552",
            "3558",
            "3564",
            "3570",
            "3576",
            "3582",
            "3588",
            "3594",
            "36",
            "360",
            "3600",
            "3606",
            "3612",
            "3618",
            "3624",
            "3630",
            "3636",
            "3642",
            "3648",
            "3654",
            "366",
            "3660",
            "3666",
            "3672",
            "3678",
            "3684",
            "3690",
            "3696",
            "3702",
            "3708",
            "3714",
            "372",
            "3720",
            "3726",
            "3732",
            "3738",
            "3744",
            "3750",
            "3756",
            "3762",
            "3768",
            "3774",
            "378",
            "3780",
            "3786",
            "3792",
            "3798",
            "3804",
            "3810",
            "3816",
            "3822",
            "3828",
            "3834",
            "384",
            "3840",
            "3846",
            "3852",
            "3858",
            "3864",
            "3870",
            "3876",
            "3882",
            "3888",
            "3894",
            "390",
            "3900",
            "3906",
            "3912",
            "3918",
            "3924",
            "3930",
            "3936",
            "3942",
            "3948",
            "3954",
            "396",
            "3960",
            "3966",
            "3972",
            "3978",
            "3984",
            "3990",
            "3996",
            "4002",
            "4008",
            "4014",
            "402",
            "4020",
            "4026",
            "4032",
            "4038",
            "4044",
            "4050",
            "4056",
            "4062",
            "4068",
            "4074",
            "408",
            "4080",
            "4086",
            "4092",
            "4098",
            "4104",
            "4110",
            "4116",
            "4122",
            "4128",
            "4134",
            "414",
            "4140",
            "4146",
            "4152",
            "4158",
            "4164",
            "4170",
            "4176",
            "4182",
            "4188",
            "4194",
            "42",
            "420",
            "4200",
            "4206",
            "4212",
            "4218",
            "4224",
            "4230",
            "4236",
            "4242",
            "4248",
            "4254",
            "426",
            "4260",
            "4266",
            "4272",
            "4278",
            "4284",
            "4290",
            "4296",
            "4302",
            "4308",
            "4314",
            "432",
            "4320",
            "4326",
            "4332",
            "4338",
            "4344",
            "4350",
            "4356",
            "4362",
            "4368",
            "4374",
            "438",
            "4380",
            "4386",
            "4392",
            "4398",
            "4404",
            "4410",
            "4416",
            "4422",
            "4428",
            "4434",
            "444",
            "4440",
            "4446",
            "4452",
            "4458",
            "4464",
            "4470",
            "4476",
            "4482",
            "4488",
            "4494",
            "450",
            "4500",
            "4506",
            "4512",
            "4518",
            "4524",
            "4530",
            "4536",
            "4542",
            "4548",
            "4554",
            "456",
            "4560",
            "4566",
            "4572",
            "4578",
            "4584",
            "4590",
            "4596",
            "4602",
            "4608",
            "4614",
            "462",
            "4620",
            "4626",
            "4632",
            "4638",
            "4644",
            "4650",
            "4656",
            "4662",
            "4668",
            "4674",
            "468",
            "4680",
            "4686",
            "4692",
            "4698",
            "4704",
            "4710",
            "4716",
            "4722",
            "4728",
            "4734",
            "474",
            "4740",
            "4746",
            "4752",
            "4758",
            "4764",
            "4770",
            "4776",
            "4782",
            "4788",
            "4794",
            "48",
            "480",
            "4800",
            "4806",
            "4812",
            "4818",
            "4824",
            "4830",
            "4836",
            "4842",
            "4848",
            "4854",
            "486",
            "4860",
            "4866",
            "4872",
            "4878",
            "4884",
            "4890",
            "4896",
            "4902",
            "4908",
            "4914",
            "492",
            "4920",
            "4926",
            "4932",
            "4938",
            "4944",
            "4950",
            "4956",
            "4962",
            "4968",
            "4974",
            "498",
            "4980",
            "4986",
            "4992",
            "4998",
            "5004",
            "5010",
            "5016",
            "5022",
            "5028",
            "5034",
            "504",
            "5040",
            "5046",
            "5052",
            "5058",
            "5064",
            "5070",
            "5076",
            "5082",
            "5088",
            "5094",
            "510",
            "5100",
            "5106",
            "5112",
            "5118",
            "5124",
            "5130",
            "5136",
            "5142",
            "5148",
            "5154",
            "516",
            "5160",
            "522",
            "528",
            "534",
            "54",
            "540",
            "546",
            "552",
            "558",
            "564",
            "570",
            "576",
            "582",
            "588",
            "594",
            "6",
            "60",
            "600",
            "606",
            "612",
            "618",
            "624",
            "630",
            "636",
            "642",
            "648",
            "654",
            "66",
            "660",
            "666",
            "672",
            "678",
            "684",
            "690",
            "696",
            "702",
            "708",
            "714",
            "72",
            "720",
            "726",
            "732",
            "738",
            "744",
            "750",
            "756",
            "762",
            "768",
            "774",
            "78",
            "780",
            "786",
            "792",
            "798",
            "804",
            "810",
            "816",
            "822",
            "828",
            "834",
            "84",
            "840",
            "846",
            "852",
            "858",
            "864",
            "870",
            "876",
            "882",
            "888",
            "894",
            "90",
            "900",
            "906",
            "912",
            "918",
            "924",
            "930",
            "936",
            "942",
            "948",
            "954",
            "96",
            "960",
            "966",
            "972",
            "978",
            "984",
            "990",
            "996",
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
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "10m_wind_gust_since_previous_post_processing",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "eastward_turbulent_surface_stress",
            "evaporation",
            "land_sea_mask",
            "maximum_2m_temperature_in_the_last_24_hours",
            "mean_sea_level_pressure",
            "minimum_2m_temperature_in_the_last_24_hours",
            "northward_turbulent_surface_stress",
            "orography",
            "runoff",
            "sea_ice_cover",
            "sea_surface_temperature",
            "snow_density",
            "snow_depth",
            "snowfall",
            "soil_temperature_level_1",
            "sub_surface_runoff",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_thermal_radiation",
            "surface_runoff",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downwards",
            "toa_incident_solar_radiation",
            "top_net_solar_radiation",
            "top_net_thermal_radiation",
            "total_cloud_cover",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_water_vapour",
            "total_precipitation",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "2023",
        ],
        multiple=True,
    )
    @normalize(
        "originating_centre",
        [
            "cmcc",
            "dwd",
            "eccc",
            "ecmwf",
            "jma",
            "meteo_france",
            "ncep",
            "ukmo",
        ],
    )
    @normalize(
        "system",
        [
            "1",
            "12",
            "13",
            "14",
            "15",
            "2",
            "21",
            "3",
            "35",
            "4",
            "5",
            "51",
            "6",
            "600",
            "601",
            "602",
            "7",
            "8",
        ],
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        day,
        leadtime_hour,
        month,
        variable,
        year,
        originating_centre,
        system,
        format_,
        area=None,
    ):
        super().__init__(
            day=day,
            leadtime_hour=leadtime_hour,
            month=month,
            variable=variable,
            year=year,
            originating_centre=originating_centre,
            system=system,
            format_=format_,
            area=area,
        )
