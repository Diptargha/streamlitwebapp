"""This is the top-level package for the probabilistic stability modelling tool.

NOTE: This package is a work-in-progress. Currently only the stability automation subpackage "pfstability" is
functional.

This package containts the following subpackages:

app: This will contain code used for operating the model through a user interface.
data: This will be used to store and access input data.
jointdist: This will be used for finding the joint distribution of inputs (if viable).
pfstability: This runs snapshots through power factory RMS stability studies
sensitivity: This will be used for undertaking sensitivity analysis of a network, to aid its reduction (if viable).
stability: This will be a wrapper on the power factory studies, integrating efficient methods such as active learning.
"""
