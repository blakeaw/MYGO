"""PySB version of simple model of yeast glycolytic oscillations from Bier et al.

"""

# PySB components
from pysb import (
    Model,
    Monomer,
    Parameter,
    Initial,
    Rule,
    Observable,
    Expression,
    Annotation,
    ANY,
    WILD,
)

from pysb.macros import synthesize, degrade

## Initialize the model.
Model()

## Define the monomers.

# Glucose
Monomer("G")
# ATP
Monomer("ATP")

## Initials

Parameter("G_0", 3.1)
Parameter("ATP_0", 3.4)
Initial(G(), G_0)
Initial(ATP(), ATP_0)

## Define the model rules.

### Glucose transport
Parameter("Vin", 0.36)
# model the transport term as a zero-order synthesis
synthesize(G(), Vin)

### Phosphofrutokinase - glucose to ATP catalyzed by ATP
Parameter("k1", 0.02)
# Consumes 1 glucose and generates 2 net ATP.
Rule("phosphofrutokinase", G() + ATP() >> ATP() + ATP() + ATP(), k1)

### ATPases
Parameter("kp", 6)
Parameter("Km", 13)
Observable("oATP", ATP())
Expression("_kp", kp / (oATP + Km))
degrade(ATP(), _kp)

Observable("oG", G())
