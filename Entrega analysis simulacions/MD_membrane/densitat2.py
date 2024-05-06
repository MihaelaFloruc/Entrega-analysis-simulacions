import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt

u = mda.Universe('input/dppc_water.psf', 'input/initial_coordinates.pdb', 'simulation_NpT/NpT.dcd', dt=10.0)

aigua = u.select_atoms("resname TIP3")
carbonatades = u.select_atoms("resname DPPC")

radio_corte =50

densitats_aigua = []
temps= []

for ts in u.trajectory:
    temps_actual = u.trajectory.time
    temps.append(temps_actual)

    coordenades_aigua = aigua.positions
    coordenades_carbonatades = carbonatades.positions

    distancies = np.linalg.norm(coordenades_aigua[:, np.newaxis,:] - coordenades_carbonatades, axis=2)

    num_aigues_aprop = np.sum(distancies < radio_corte, axis=0)

    densitat_aigua=num_aigues_aprop/len(aigua)
    densitats_aigua.append(densitat_aigua)

densitats_aigua = np.array(densitats_aigua)
temps = np.array(temps)

densitat_mitja_temps = np.mean(densitats_aigua, axis=1)

plt.plot(temps, densitat_mitja_temps)
plt.xlabel('Temps (ps)')
plt.ylabel('Densitat aigua (molt/A³)')
plt.title('Densitat aigua en funció del temps')
plt.show()
