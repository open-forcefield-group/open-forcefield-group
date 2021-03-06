import pandas as pd
from rdkit.Chem import PandasTools

data = pd.read_hdf("./data.h5", "data")
PandasTools.AddMoleculeColumnToFrame(data, smilesCol='smiles', molCol='molecule', includeFingerprints=False)
data = data.set_index("CAS")
data[["density", "Temperature", "molecule"]]
