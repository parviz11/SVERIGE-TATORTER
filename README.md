# Sweden's urban areas map

According to SCB ([Statistics Sweden](https://www.scb.se)), urban area ("tätorter" in Swedish) is defined as the area with the population more than 200 people. The borders are defined by [Lantmäteriet](https://www.lantmateriet.se). The data was downloaded from [SCB open database](https://www.scb.se/vara-tjanster/oppna-data/oppna-geodata/tatorter/). The most recent data is from 2020.

### Use cases:
* Analytical web app with customer geolocations inside urban areas
* Enrich existing customer data with geolocations
* Build ML models with geolocations.

### Main challenge
Urban areas are recorded as polygons with high accuracy for borders. This makes the database itself very large to handle with simple calls. For example, loading data takes long time. Find a way to load large data fast to make interactive UI (web app). Alternatively, load data only once and have the borders always active in the web app. The latter would make user experience unpleasant and can cause lower user activity.
