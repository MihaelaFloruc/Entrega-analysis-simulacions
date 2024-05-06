import MDAnalysis as mda
from MDAnalysis.analysis import density
import numpy as np

u = mda.Universe('input/dppc_water.psf', 'input/initial_coordinates.pdb', 'simulation_NpT/NpT.dcd', 'simulation_NpT/NpT.coor')

aigua = u.select_atoms("resname TIP3")
carbonatades = u.select_atoms("resname DPPC")

print(aigua)
densitat_graella = density.DensityAnalysis(u, aigua, 1.0)
densitat_graella.run()

densitat_aigua=[]
for ts in u.trajectory:
    densitat_aigua = densitat_graella.grid.interpolate(carbonatades.positions)
    densitat_aigua.append(densitat_aigua)

densitat_mitja = np.mean(densitat_aigua)
desviacio_estandard = np.std(densitat_aigua)

print("Densitat mitjana d'aigua al voltant de les cadenes carbonatades", densitat_mitja, "mol/A³")
print("Desviació estàndard de la densitat d'aigua", desviacio_estandard, "mol/A³" )
