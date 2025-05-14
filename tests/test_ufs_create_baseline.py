import time
from dataclasses import dataclass
from pathlib import Path

import dask.array as da
import pytest

import xarray as xr

from monetio.models._rrfs_cmaq_mm import open_mfdataset


def test_create_baseline() -> None:
    rootdir = Path("/opt/project/local-data")
    outdir = rootdir / f"baseline-{int(time.time())}"
    baseline = outdir / "baseline-20250514.nc"

    outdir.mkdir(exist_ok=False)
    for dynfile in rootdir.glob("aqm.t12z.dyn.f*.nc"):
        with xr.open_dataset(dynfile) as dset:
            subset = dset.isel({"grid_xt": slice(380, 392), "grid_yt": slice(240, 251)})
            subset.to_netcdf(outdir / dynfile.name)

    actual = open_mfdataset(str(outdir / "aqm.t12z.dyn.f*.nc"))
    actual.to_netcdf(baseline)

    for name, array in actual.data_vars.items():
        print(name)
        df = array.to_dataframe()
        print(df[name].describe())
