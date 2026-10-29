# Fixture C4 — invented Methods paste: regression discontinuity

> **Fiction.** The policy, data and numbers are invented to test methods-decomposer.

**3.2 Empirical design (fictitious)**

Under a 2015 national rule, cities with an urban population of at least 500,000 must install real-time air-quality monitoring stations and publish hourly readings. We exploit this threshold in a regression discontinuity design using 612 cities. The running variable is 2014 urban population (P_c), centred at 500,000. We estimate

PM_c = α + τ D_c + f(P_c) + D_c · g(P_c) + ε_c

where D_c = 1 if P_c ≥ 500,000, and f and g are fourth-order polynomials estimated on the full sample. τ is the effect of information disclosure on PM2.5 concentration in 2017. Cities just above the threshold also became eligible for central "Civilised City" funding in 2015. Results are robust to using third-order polynomials.
