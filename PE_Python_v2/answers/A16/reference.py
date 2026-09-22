import pandas as pd
import h5py
from scipy.io import loadmat
def read_science(path,kind):
    if kind=="stata": return pd.read_stata(path)
    if kind in ("sas7bdat","xport"): return pd.read_sas(path,format=kind,encoding="utf8")
    if kind=="hdf5":
        with h5py.File(path,"r") as handle: return handle["scores"][()]
    if kind=="mat": return loadmat(path)["scores"]
    raise ValueError("kind")
