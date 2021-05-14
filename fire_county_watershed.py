# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:15:27 2021

@author: Rebecca
"""
# Import modules as necessary

import geopandas
import matplotlib.pyplot as plt


# Part 1: Load the HUC 8 Watershed files and limit to the relevant watersheds
# New Mexico: Rio Chama, Upper Rio Grande, Jemez, Rio Grande-Santa Fe

# Load the zip file name to your state watershed variable
nm_watersheds = 'zip://wbdhu8_a_nm.zip'

watersheds = geopandas.read_file(nm_watersheds)

# Limit watersheds to those that are relevant
names = ['Rio Chama', 'Jemez', 'Upper Rio Grande', 'Rio Grande-Santa Fe']

fire_zone = watersheds['Name'].isin(names)

# Create a dataframe of the watersheds in the fire zone
on_watersheds = watersheds[fire_zone]

# Write the watersheds layer to a geopackage to load in GIS
on_watersheds.to_file('watersheds.gpkg',layer='watersheds',driver='GPKG')

#%%
# Part 2: Load the NM Census County shapefiles

# Load the county zip file to your county variable
nm_counties = 'zip://tl_2010_35_county10.zip'

counties = geopandas.read_file(nm_counties) 

# Show how many counties are in the state
print( '\nTotal number of New Mexico counties:')
print( len(counties['NAME10']))

# Write the counties to a geopackage
counties.to_file('nm_counties.gpkg',layer='counties',driver='GPKG')

#Then connect the counties to the watersheds in a spatial join

# Join the counties onto the watersheds
watershed_counties = geopandas.sjoin(counties,
                                     on_watersheds,
                                     how="inner",
                                     op='intersects')

# Drop the right index column - you won't need it
watershed_counties = watershed_counties.drop(columns=['index_right'])

# Write the joined data to a CSV and a geopackage on the counties variable
watershed_counties.to_csv('watershed_counties.csv')

watershed_counties.to_file('watershed_counties.gpkg',layer='counties',driver='GPKG')

# Identify the list of county names that are included without duplicates
county_names = set(watershed_counties['NAME10'])

# Show how many counties total intersect with the watersheds
print( '\nNumber of counties intersecting with the NM Watersheds:')
print(len(watershed_counties['NAME10']))

# Show the names of these counties 
print( '\nNew Mexico counties that intersect with the watersheds:')
print(county_names)


#%%
# Part 3: Load the wildfire perimeter data, which also includes the other information

# Load the wildfire zip file into your wildfire variable
nm_wildfire = 'zip://wildfire_perim_1911_2014.zip'

wildfire = geopandas.read_file(nm_wildfire)

# Make the year column a float instead of a string
wildfire['FIRE_YEAR'] = wildfire['FIRE_YEAR'].astype(float)

# Limit data to the fires that happened before your chosen year 
is_recent = wildfire['FIRE_YEAR'] > 1999

wildfire = wildfire[is_recent]

# Write the wildfire data to a csv and geopackage to display all the fires in that time
wildfire.to_csv('wildfire.csv')

wildfire.to_file('wildfire.gpkg',layer='wildfire',driver='GPKG')

# Set the projection of the wildfire data
x = wildfire.to_crs(epsg=4269)

# Do a spatial join with intersects of the county watershed data to the fire data
# Using the variable that set the projection
wildfire_counties = geopandas.sjoin(x,
                                    watershed_counties,
                                    how="inner",
                                    op='intersects')

# Display the number of fires in the year span of the dataset
print('\nNumber of wildfires in NM 2000-2014:')
print(len(wildfire))

# Display the number of fires in the counties in the watersheds in those years
print('nNumber of wildfires in counties affected by Las Conchas Fire since 2000:')
print(len(wildfire_counties))

# Write this dataframe to a CSV and a geopackage using the wildfire layer
wildfire_counties.to_csv('wildfire_counties.csv')

wildfire_counties.to_file('wildfire_counties.gpkg',layer='wildfire',driver='GPKG')



#%%

# Part 4: Load the American Community Survey demographic data: income
# Just for latest year - 2018

# Load the ACS zip file to the income variable
acs_income = 'zip://incomeearn_byco2017.zip'
income = geopandas.read_file(acs_income)

income.to_file('2017_income.gpkg',layer='income',driver='GPKG')

# Limit the counties to the ones you identified previously
inc_co = income['NAME10'].isin(county_names)
county_inc = income[inc_co]

#Create a bar graph of average household income by county
fig, ax1 = plt.subplots()

county = county_inc['NAME10']
hh_inc = county_inc['MEDINCTOTU']

plt.barh(county,hh_inc, color=['rebeccapurple','violet','turquoise','green','coral','gold'])
fig.suptitle("Average Household Income by County (2017)")
ax1.set_title(None)
ax1.set_ylabel("County")
ax1.set_xlabel("$USD")
fig.tight_layout()

fig.savefig('hhinc_nmcounty.png',dpi=300)

# Part 5: Load the American Community Survey demographic data: population
# Just for latest year - 2018
import geopandas
import matplotlib.pyplot as plt

# Load the population data file to the pop variable
nm_2017pop = 'zip://popul_byco2017.zip'
pop_2017 = geopandas.read_file(nm_2017pop)

# Clean up the data to have the column names you need
pop = pop_2017.rename(columns={'cowntee_NA':'county'})

pop.to_file('2017_pop.gpkg',layer='pop_2017',driver='GPKG')

# Limit the counties to the ones you identified previously
pop_counties = pop['county'].isin(county_names)
county_pop = pop[pop_counties]

# Make the population column a float instead of a string
county_pop['popul_byco'] = county_pop['popul_byco'].astype(float)

#Create a bar graph of average household income by county
fig, ax1 = plt.subplots()

county = county_pop['county']
tot_pop = county_pop['popul_byco']

plt.barh(county,tot_pop, color=['teal','gold','salmon','orchid','pink'])
fig.suptitle("Population by County (2017)")
ax1.set_title(None)
ax1.set_ylabel("County")
ax1.set_xlabel("Number of people")
fig.tight_layout()

fig.savefig('2018pop_nmcounty.png',dpi=300)