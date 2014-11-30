Data Analysis
=============

I'll describe here how I image the data analysis process will look like:

Get the Data:
-------------

* Every hour the system will try to get a more recent data from WOW API on the auctions of all registered Realms;
* This auction's data will be saved with the timestamp of the `last_modified` field from WOW API;

Analysis:
---------

When a user, ask for the tracked item (ex: `#12345`), it will:

    * get the realm it's been asked for;
    * get the datetime for the latest 30 days, counting on today;
    * For each day, it will first try to check if the information is already saved in a Django Model (PostgreSQL), this will happen if the analysis for that day/realm/item was already done;
    * if the information is not present in PostgreSQL, then search the MongoDB's data and get all the auctions.json of that day;
        * after that, it will go through each `auctions.json`, and get the `Avarage Price` and the `User Price` for the tracked item (ex: #12345);
        * then it will make the `avarage` for the hole day with the `Avarage Price` of each `auction.json`, and the same thing with the `User Price`.
        * will save this information in a Django Model (PostgreSQL), to make it easy to retrieve, and don't re-do work.
