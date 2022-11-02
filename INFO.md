# broadband II

## project goals

* Integrate socioeconomic data from census.gov to assess the societal problem identified by the stakeholder
* Provide information for county subdivisions in Maine (stakeholder request)
* Improve performance of the interactive map in the original broadband project

## broadband I

* Student repo (spring 2022): https://github.com/ds5010/broadband
* Student github-pages site (spring 2022): https://ds5010.github.io/broadband
* Yune repo (summer 2022): https://github.com/ds5110/project-zyune

## Background

* [Purdue site](https://www.benton.org/source/purdue-university)
* [Digital divide in the US](https://www.benton.org/headlines/digital-divide-us)
  * This page provides a quick overview of the societal problem
  * I got the link to this site in an email from Meghan (Sep 2022)
  * The recommendation for this site originated w/Maggie Drummond-Bahl -- colleague at MCA

## FCC data

* [FCC Form 477 data](https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477)
  * Broadband deployment data are available by state from this link
* CSV download for Maine: https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477
  * This file must be downloaded by hand as a zip file (i.e. requires a button click)
* GEOID: The CSV has a BlockCode column with a 15-digit block code (e.g., 230050111004026) 

## Census.gov geography

* [./src/gpd.py](./src/gpd.py) -- downloads county-subdivision shapefile for Maine and converts to geojson
  * This code can be run in Colab if you can't get geopandas to install locally
  * [geopandas](https://geopandas.org/en/stable/index.html) -- geopandas.org
  * latest version is 0.12 as of Oct 2022
* Census blocks for Maine
  * https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/tl_2022_23_tabblock20.zip

## geopandas install

These instructions for using conda environments is recommended for geopandas, which can be a challenge to install.

* [Geopandas installation](https://geopandas.org/en/stable/getting_started/install.html) can create dependency conflicts.
* Therefore you may want to [Create a conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for geo-data local processing with geopandas
  * Conda environments are isolated and easy to remove if you need to start over.
  * The following commands assume you have conda or miniconda installed already.
* List environments that exist locally
```
conda env list
```
* Create a "geo" environment that includes geopandas
```
conda create --name geo 
conda activate geo
conda install geopandas
```
* Or, [create an environment from a .yml file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) with one line:
```
conda env create -n geo --file environment.yml
```
* When you're done using geopandas, deactivate the environment:
```
conda deactivate
```
* To remove the environment:
```
conda deactivate
conda env remove --name geo
```
* Conda references
  * [conda user guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/index.html)
  * [conda tasks](https://conda.io/projects/conda/en/latest/user-guide/tasks/index.html)
  * [conda cheat sheet](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
  * [creating an environment.yml file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment)
  * [conda install](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Maine GIS

* [Maine GeoLibrary](https://www.maine.gov/geolib/) -- maine.gov
  * Entry point for data catalog and services
* [Maine Census Tracts (2010)](https://maine.hub.arcgis.com/datasets/e7a7e490a9bf4bc08c7507f7aabe0f8a) -- arcgis.com

## GEOIDs

* [Understanding GEOIDs](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html) -- census.gov
  * This link is a great reference!
  * FIPS -- Federal Information Processing Service
    * FIPS codes are usually unique within larger geographic entities
    * states -- 2 digits
    * counties -- 5 digits
    * places -- 7 digits
  * GNIS -- Geographic Names Information System codes...
    * do not have a "nesting relationship" as do FIPS codes
    * include airports, beaches, cemeteries, post offices, etc.
    * do not include roads and highways
    * are assigned sequentially based on date of entry
    * do not represent a geographic hierarchy
    * codes can be up to 10 digits in length
  * Census Bureau Codes
    * these census.gov codes are for areas are not covered by FIPS and GNIS
    * these areas include census divisions, census regions, census tracts, block groups, census blocks and urban areas
    * full GEOISs for many levels of geography combine both FIPS and Census Bureau codes
    * for example: census tracts, block groups and census blocks nest within state and county
      * therefore their GEOIDs contain both the state and county FIPS codes, in which they nest.
* GEOID
  * COSUB = County Subdivision (the recommendation from Meghan)
  * STATE -- 2 digits
  * STATE+COUNTY -- 5 digits
  * STATE+COUNTY+COUSUB -- 10 digits
  * STATE+COUNTY+TRACT+BLOCK GROUP -- 2+3+6+1 -- 12 digits
  * STATE+COUNTY+TRACT+BLOCK -- 2+3+6+4 -- 15 digits -- FCC uses this encoding!
* [County subdivisions](https://www2.census.gov/geo/pdfs/reference/GARM/Ch8GARM.pdf) (PDF)
  * CCD names -- Census County Division
  * The purpose of CCDs is to provide a set of subcounty units that
    * (1) have community orientation; 
    * (2) have visible, stable boundaries; 
    * (3) conform to groupings of census tracts or block numbering areas (BNAs); and 
    * (4) have a recognizable name.
* [standard hierarchy](https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf) (PDF)
  * Chart shows relationship between the various geographic entities

## FCC website

* [FCC broadband 477 map](https://broadband477map.fcc.gov/)
* mapbox application that allows lookup by street address

## FCC data

* Stakeholder recommendation: https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477
  * https://us-fcc.box.com/v/ME-Jun2021-v1
  * Download (by hand) the 3.2 M zip file -- unzips into 80MB file
* The geospatial info is a 15-digit census block code
  * [data dictionary](https://www.fcc.gov/general/explanation-broadband-deployment-data)
  * [More about Census blocks (pdf)](https://transition.fcc.gov/form477/Geo/more_about_census_blocks.pdf) -- fcc.gov
  * Column headers...
    * LogRecNo
    * Provider_Id
    * FRN
    * ProviderName
    * DBAName
    * HoldingCompanyName
    * HocoNum
    * HocoFinal
    * StateAbbr
    * BlockCode
    * TechCode
    * Consumer
    * MaxAdDown
    * MaxAdUp
    * Business
* [More about census blocks](https://transition.fcc.gov/form477/Geo/more_about_census_blocks.pdf) (PDF)
  * Census blocks have higher resolution than county subdivisions
  * But the crosswalk with between census block and county subdivision is unclear
