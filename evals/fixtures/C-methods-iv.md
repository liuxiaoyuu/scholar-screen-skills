# Fixture C3 — invented Methods paste: IV (same paper as A3 #1)

> **Fiction.** The paper, data and numbers are invented to test methods-decomposer.

**4. Identification Strategy (fictitious)**

Regulation stringency R_ct (the count of environmental enforcement actions per 1,000 firms) is likely endogenous: cities attracting more FDI may face different enforcement. We instrument R_ct with Z_ct = log(Distance_c) × Target_t, where Distance_c is the city's distance to the nearest coastline and Target_t is the national ventilation-coefficient-based pollution target in year t.

First stage:   R_ct = π Z_ct + X_ct'ψ + α_c + δ_t + v_ct        (4)
Second stage:  log(FDI_ct) = β R̂_ct + X_ct'κ + α_c + δ_t + e_ct      (5)

X_ct includes log GDP, population and road density. The first stage is strong. Because we also use a second instrument (Z_ct squared), the Hansen J test of over-identifying restrictions does not reject (p = 0.41), which confirms that the exclusion restriction holds. β is the average effect of regulation on FDI across all cities. Standard errors are clustered by province.
