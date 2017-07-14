# numpy-accumulative-histograms
Wrappers for Numpy 1D/2D histograms that allow accumulative filling.

---

Numpy histograms are meant to be used once on a complete dataset.
Sometimes, one has an event-based setup, where individual datasets are to be accumulated in the histogram successively.
This can be achieved by a simple wrapper, removing the need to hold all data in memory at the same time and allowing simple plotting of intermediate results.
