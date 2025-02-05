/* Check that the table doesn't already exist in the database. If it does,remove it from the database */
DROP TABLE IF EXISTS County_and_Disasters;

/* Create the table in the database & give it a name */
CREATE TABLE County_and_Disasters (

/* Tell the database which data to import, what its name in the database should be, & the type of data to import */
	COUNTY text,
	STATEABBRV text,
    avalanche text,
    cflooding text,
    cwave text,
    drought text,
    earthquake text,
    hail text,
    hwave text,
    hurricane text,
    istorm text,
    landslide text,
    lightning text,
    rflooding text,
    swind text,
    tornado text,
    tsunami text,
    vactivity text,
    wildfire text,
    wweather text
);
