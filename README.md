Comparative Analysis of Mean and Variability of PM2.5 Across 9 Indian Cities


OVERVIEW

This project analyses short term PM2.5 pollution patterns across multiple Indian cities using publicly available data. It compares mean PM2.5 concentration with day-to-day variabililty, highlighting differences between chronic and episodic exposure.



DATA SOURCE

⦁	PM2.5 data obtained from CPCB monitoring stations via OpenAQ.
⦁	Cities analyzed: Bangalore(Karnataka), Bhubaneswar(Odisha), Chennai(Tamil Nadu), Delhi, Jodhpur(Rajasthan), Kolkata(West Bengal), Lucknow(Uttar Pradesh), Mumbai(Maharashtra), Raipur(Chhattisgarh).
⦁	Time Window: 15-26 December 2025
⦁	Data frequency: Daily averages derived from available observations



DATA AVAILABILITY NOTES

⦁	Some hourly values of Lucknow were missing and recorded as zero in the source data, which might skew the daily averages to a lower value than the actual value.
⦁	PM2.5 values in Mumbai were unavailable from 20/12/2025 to 23/12/2025.



METHODOLOGY

For each city:
1.	Daily PM2.5 values were aggregated
2.	The mean PM2.5 values were computed
3.	Standard Deviation was computed using sample variance(n-1). We are estimating variability from a small sample, that is why we divide by (n − 1) instead of n when computing variance.
4.	Coefficient of Variation(CV) was computed as:
                                      CV=standard deviation/mean
5.CV captures relative day-to-day variability, allowing comparison between cities with different pollution baselines.



VISUALISATIONS​

⦁	Line Plot: Daily PM2.5 variation for each city.
For Mumbai, data between 20/12/2025 and 23/12/2025 were unavailable.Therefore, the plot skips directly from 19/12/2025 to 24/12/2025.
⦁	Bar plot: Mean PM2.5 concentration across cities
⦁	Scatter plot: Mean PM2.5 vs Coefficient of Variation:- Highlights differences between consistently polluted cities and cities with episodic pollution spikes


KEY OBSERVATIONS

*All observations below are comparative in nature and refer only to differences among the cities included in this analysis.*

⦁	Delhi exhibits very high mean PM2.5 concentration along with high variability.
⦁	Jodhpur shows lower mean PM2.5 but high variability, suggesting episodic pollution spikes.
⦁	Raipur, Chennai, Kolkata, and Lucknow show moderate mean PM2.5 with moderate variability.
⦁	Bhubaneswar shows comparatively moderate mean PM2.5 concentrations and low variabilty.
⦁	Mumbai and Bangalore exhibit low mean PM2.5 concentrations and low variabilty.
⦁	Mean pollution alone is insufficient to characterize exposure risk.



LIMITATIONS

⦁	Short analysis window (12 days)
⦁	Missing data for certain cities may affect variability estimates
⦁	No meteorological factors included(eg. wind speed, wind direction, humidity, rainfall, temperature etc.)



PUBLIC HEALTH CONTEXT

⦁	Even cities with comparatively lower PM2.5 concentrations still exceed the WHO recommended limits by a large margin, indicating that “lower” pollution levels do not necessarily imply safe air quality.
