# Guides of using the DB and the data

## Abstract
This markdown file was created to explain about the usage of the DB, <br />
and the data in the Heroes project. <br />

## DB - Mongo
### Why Mongo DB
For this project we used in Mongo DB to store our data. We chose this <br />
DB because:
1. It's a simple and easy to manage DB which fits to the timeline of <br />
   Hackathon.
2. It's a non-relational documentary DB. Our data is easy to represent <br />
   as documents, and the flexibility that it provide helps us to br more <br />
   agile.
3. Powerful community and vast stack of existing packages to use.
4. Scalable to future purposes

### DB Usage Implementation
We downloaded the Mongo Db from the [official website of Mongo DB](https://www.mongodb.com/try/download/community). <br />
After the download and the installation, all we need to do is to ```cd``` to <br />
directory of the Mongo DB files and that activate the relevant script <br />
to initialize and start the DB.

## Mongo Handler & Pymongo
To interact with Mongo Db we used in package named **pymongo**. It's <br />
provide us very easy way to handle with the Mongo DB. <br />
You can download with the command ```pip install pymongo``` <br />

## How to use
We already implemented the relevant functions. If you want to <br />
change some questions or images, modify the JSONs files under <br />
heros / jsons and then use the repopulate functions to update <br />
the relevant collections.
