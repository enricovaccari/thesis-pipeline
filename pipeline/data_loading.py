# 04_Code/pipeline/data_loading.py
"""
Data loading utilities for the AMOC thesis project.
Centralizes dataset opening and unit conversion so every notebook
works with consistent, Sverdrup-denominated data.
"""

import xarray as xr

from pipeline.paths import (
    COPERNICUS_AMOC,
    RAPID_TRANSPORTS,
    RAPID_VERTICAL,
)

# Sverdrup conversion: 1 Sv = 1e6 m³/s
M3S_TO_SV = 1e6


def load_copernicus(convert_to_sv=True):
    """
    Load the Copernicus OMI AMOC dataset.

    Copernicus is distributed in raw SI units (m³/s). When convert_to_sv
    is True (default), all AMOC variables are converted to Sverdrups and
    their unit metadata is updated for self-consistency.
    """
    ds = xr.open_dataset(COPERNICUS_AMOC)

    if convert_to_sv:
        amoc_vars = ['amoc_cglo', 'amoc_glor', 'amoc_oras', 'amoc_mean', 'amoc_std']
        for var in amoc_vars:
            if var in ds:
                ds[var] = ds[var] / M3S_TO_SV
                ds[var].attrs['units'] = 'Sv'
                ds[var].attrs['conversion_note'] = (
                    'Converted from m3 s-1 to Sv (1 Sv = 1e6 m3 s-1)'
                )
    return ds


def load_rapid_transports():
    """
    Load the RAPID transports dataset.
    RAPID is distributed natively in Sverdrups — no conversion needed.
    """
    return xr.open_dataset(RAPID_TRANSPORTS)


def load_rapid_vertical():
    """
    Load the RAPID vertical structure dataset (stream function).
    Native units are Sverdrups.
    """
    return xr.open_dataset(RAPID_VERTICAL)