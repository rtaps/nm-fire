# Using New Mexico Wildfire, Watershed, and Demographic Data to Inform Adaptive Management 

## Summary
------
In June of 2011, the Las Conchas fire burned 156,593 acres in northern New Mexico before being contained on August 1st. Of that acreage, 43,000 were engulfed within the first 14 hours of spread, making it at the time the largest wildfire in the state’s history. It threatened the Los Alamos National Laboratory, and burned part of Santa Fe National Forest, several local Pueblos, the town of Los Alamos, Bandelier National Monument, and the Caldera National Preserve. 

Las Conchas was of great concern to the managers of the nearby Santa Fe Municipal Watershed (SFMW), whose territory encompasses 17,384 acres in the upper reaches of the Santa Fe River basin. The water filtered by and flowing through this system supplies 30,000 homes and businesses in and around the City of Santa Fe – approximately 40% of its water supply. 

Following the 2011 fires, Santa Fe implemented a 19-year adaptive watershed management plan that has used controlled burns, vegetation reduction and other methods to restore the forest condition and reduce the incidence of large, intense fires. 

This repository contains a script that uses the Las Conchas fire as a case study to identify: 
 
..-Which watersheds are affected by a particular fire; 
..-Which counties intersect with those watersheds; 
..-What fires have occurred within those units; 
..-The demographic information of the people in those counties. 

The goal of this script is to be translatable to fires in any state in the U.S. with access to comparative data for managers who would like to target adaptive management techniques to certain geographic units that are greatest risk. 

## Input Data 
------
One script (fire_county_watershed.py), three shapefiles, and two csv as follows:

1. Census TIGER/Line County Shapefiles
    ..Follow the Web Interface Link at the [Census site](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html),
    ..Select the Year 2010 and the Counties (and equivalent) layer type,
    ..After hitting submit, select New Mexico in the 2010 dropdown menu and download the file.
    
The remaining files are available from the [NM RGIS Database](https://rgis.unm.edu/rgis6/)    

2. [USGS HUC 8 (Sub-basin) Watershed Shapefiles](https://rgis.unm.edu/rgis6/dataset.html?uuid=cae16e7f-c3d1-4264-b14b-f1c6db755a88)
            
3. [1911-2014 New Mexico Wildland Fire Perimeter Shapefiles](https://rgis.unm.edu/rgis6/dataset.html?uuid=29b84830-1fd2-44dd-a8f7-1b824dee2797)

4. [American Community Survey 2017 Income CSV](https://rgis.unm.edu/rgis6/dataset.html?uuid=f82f2633-574f-4e5f-99dc-603db9849887)

5. [American Community Survey 2017 Population CSV](https://rgis.unm.edu/rgis6/dataset.html?uuid=cd10009e-a79f-4de5-a12c-87bb5b499e9f)


## Instructions
------
### Part 1: Downloading the Data and Generating Outputs 

1. Download the input data as detailed above.

2. Run the script..
    i. The script will load the zip files, limit the data to relevant geographic units, and use spatial joins to determine which counties are most relevant to the analysis. 
    
    ii. It will then write each layer to geopackage files to be loaded into QGIS. 
    
    iii. The script will output the total number of counties, the number of counties that intersect with the watershed boundaries, and the names of those counties. 
    
    iv. It will limit the wildfire data to the years after 1999. 
    
    v. It will join the wildfire data onto the watershed county data and write the result to a geopackage. 
    
    vi. The script will output the total number of fires in that time period, as well as the number of fires that occurred in the joined counties. 
    
    vii. The script will then load the ACS income and population data, limit them to the same counties and write that information to two geopackages. 
    
    viii. It will output two graphs as png files: average household income by county and population by county. 

3. Confirm that the geopackages and two image files were created. 

### Part 2: Visualizing the Data 

1. Add new vector layers for each of the geopackages produced by the script. 

2. Filter and select the layers as desired to see the interactions between fires, watershed boundaries, county boundaries, and income/population data. 

3. Export your desired map layers as a png to save them. 

## Notes

1. Future examinations of data using this script could include tracking the size of fire area over time. The limited post-2011 nature of this wildland fire dataset made it difficult to implement as results of management are primarily seen in the long-term, but as data post-2014 comes available it would be useful to revisit with this script. 

2. Census demographic data could also be accessed using a [Census API](https://api.census.gov/data/key_signup.html).

3. Many thanks to [Professor Pete Wilcoxen](https://www.maxwell.syr.edu/wilcoxen/) for a killer semester under very challenging circumstances! 