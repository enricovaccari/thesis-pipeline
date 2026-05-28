# 04_Code/pipeline/paths.py

"""
Centralized path management for the AMOC thesis project.
All paths are derived from PROJECT_ROOT to keep the code portable.
"""

from pathlib import Path

# Project root: two levels above this file
# pipeline/paths.py → 04_Code/ → 04_Activation_Phase/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
DATA_ROOT = PROJECT_ROOT / "03_Data"
DATA_RAW = DATA_ROOT / "raw"
DATA_PROCESSED = DATA_ROOT / "processed"
DATA_OUTPUTS = DATA_ROOT / "outputs"

# Specific raw data files
COPERNICUS_DIR = DATA_RAW / "Copernicus"
RAPID_DIR = DATA_RAW / "RAPID"

COPERNICUS_AMOC = COPERNICUS_DIR / "GLOBAL_OMI_NATLANTIC_amoc_max26N_timeseries.nc"
RAPID_TRANSPORTS = RAPID_DIR / "moc_transports.nc"
RAPID_VERTICAL = RAPID_DIR / "moc_vertical.nc"


def check_data_paths():
    """Verify all expected data files are accessible."""
    paths_to_check = {
        "Copernicus AMOC timeseries": COPERNICUS_AMOC,
        "RAPID transports": RAPID_TRANSPORTS,
        "RAPID vertical": RAPID_VERTICAL,
    }
    
    for name, path in paths_to_check.items():
        status = "✓" if path.exists() else "✗ MISSING"
        print(f"{status}  {name}: {path}")