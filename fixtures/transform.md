# DailyTemperature 2026.1 transformation
Input: StationObservations version 1.0, SHA-256 3b2373075c4819348b9e5aa2b02b9fa0d9b4ceea8fc154e3ef2dea89d0140d25.
Output: DailyTemperature version 2026.1, SHA-256 4087ccfe449e713786b38ce403645ed10743c4432ea299f355c1219b17ea2381.
Group rows by UTC date and compute the arithmetic mean of temperature_c in Celsius.
All input rows participate; there is no filtering or external enrichment.
Parameters: group column=date; value column=temperature_c; aggregate=arithmetic mean; unit=Celsius; timezone=UTC.
For 2026-10-01: (28+30)/2=29. No additional upstream datasets are used.
