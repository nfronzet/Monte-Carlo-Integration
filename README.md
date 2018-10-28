# Monte-Carlo-Integration
Python program for computation and graphing of integrals computed with the Monte Carlo integration method. Supports functions of 1 and 2 variables.

The program currently does not support function insertion through string parsing.
The integrand function must be written in the definitions of "integrand" (function of 1 variable) and/or "integrand3d" (functions of 2 variables).

FUNCTIONS USAGE:

MCIntegrate(f, nTrials, PPT, t1, t2): Monte Carlo integration of function f (1 variable), computing by averaging the result of nTrials trials (each trial using PPT points per trial) between [t1,t2].
MCIntegrate3d(f, nTrials, PPT, x1, x2, y1, y2): Monte Carlo integration of function f (2 variables), computing by averaging the result of nTrials trials (each trial using PPT points per trial) between [x1,x2] and [y1,y2].
