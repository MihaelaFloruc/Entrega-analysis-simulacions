import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt

u = mda.Universe('input/dppc_water.psf', 'input/initial_coordinates.pdb', 'simulation_NpT/NpT.dcd', dt=10.0)

aigua = u.select_atoms("resname TIP3")
carbonatades = u.select_atoms("resname DPPC")

distancia_corte =10

densitats_aigua = []
temps= []

for ts in u.trajectory:
    temps_actual = u.trajectory.time
    temps.append(temps_actual)

    interficie = aigua.select_atoms(f"around {distancia_corte} resname DPPC")

    densitat_aigua = len(interficie)/(distancia_corte)
    densitats_aigua.append(densitat_aigua)

densitats_aigua = np.array(densitats_aigua)
temps = np.array(temps)

plt.plot(temps, densitats_aigua)
plt.xlabel('Temps (ps)')
plt.ylabel('Densitat aigua (molt/A³)')
plt.title('Densitat aigua en funció del temps')
plt.show()
