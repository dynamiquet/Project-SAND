/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS COUNTY_AND_RISKVALUES;

/* Create the table in the database & give it a name */
CREATE TABLE COUNTY_AND_RISKVALUES (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	COUNTY text,
	STATEABBRV text,
    AVALANCHE text,
    COASTALFLOODING text,
    COLDWAVE text,
    DROUGHT text,
    EARTHQUAKE text,
    HAIL text,
    HEATWAVE text,
    HURRICANE text,
    ISOLATEDSTORM text,
    LANDSLIDE text,
    LIGHTNING text,
    RIVERFLOODING text,
    STRINGWIND text,
    TORNADO text,
    TSUNAMI text,
    VOLCANO text,
    WILDFIRE text,
    WINTERWEATHER text
);