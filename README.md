
# hw-broadband

## assignment

* Write a Python script that computes the average maximum advertised download speed for census blocks for Millinocket.
* Millinocket is one of the county subdivisions in Maine.
* [INFO.md](INFO.md) provides all the background necessary for this assignment.
* Use the speeds reported in the FCC Form 477 data, which you can download from the link in [INFO.md](INFO.md).
* Use `crosswalk.json` to identify the census blocks by GEOID within each county subdivision in Maine.

## crosswalk.json

The data model for the "crosswalk.json" file:
```
{ county_subdivision_0,
  name: String,
  blocks: [
    String,
    String,
    ...
  ],
  county_subdivision_1
  name: String,
  blocks: [
    String,
    String,
    ...
  ],
  ...
}
```
* The county-subdivision keys (e.g., county_subdivision_0) in this data object are the 8-digit FIPS codes COUNTY+COUSUB as described in [INFO.md](INFO.md).
* The JSON data file includes all county subdivisions in Maine.
* The "name" property in the JSON file has the name of each subdivision.
* The "blocks" property is a list of GEOIDs for all census blocks in the corresponding county subdivision.
