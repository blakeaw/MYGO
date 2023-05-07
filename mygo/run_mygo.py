from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt
from .bier_simple import model


tspan = np.arange(0, 60*10)
print("Simulating...")
yfull = ScipyOdeSimulator(model).run(tspan=tspan).all

tspan_min = tspan / 60
plt.plot(tspan_min, yfull['oG'], label='[G]')
plt.plot(tspan_min , yfull['oATP'], label='[ATP]')
plt.ylabel("Concentration (uM)")
plt.xlabel("Time (min.)")
plt.legend(loc='upper left')
plt.show()