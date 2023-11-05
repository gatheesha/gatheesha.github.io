+++
title = "MySQL Cheat Sheet (For A/L Dummies)" 
date = "2023-11-05"
author = "gath"
description ="AL walta enna puluwan mysql commands list ekak."
+++



## DDL - Data Defitinion Language
### Creating Databases
### Creating Tables
### Modifying Tables

{{<highlight mysql "linenos=table,linenostart=1">}}
### CREATING DATABASES
CREATE DATABASE zoo; #Make a new databse, obviously lol
SHOW DATABASES;
USE zoo;

SHOW TABLES; 
DESCRIBE animal; #info about a specified table.

DROP DATABASE zoo; #To delete a database.
DROP TABLE animal; #To delete a table.

### CREATING TABLES
CREATE TABLE animal (  
  id INT NOT NULL, 
  name VARCHAR(64),  
  species VARCHAR(64),  
  age INT,  
  habitat_id INT,  
  FOREIGN KEY (habitat_id) REFERENCES habitat(id)  
);

### MODIFIYING TABLES
# Use the `ALTER TABLE` to modify the table structure. Not the data itself
# `ALTER TABLE` with `ADD` adds stuff to the table
ALTER TABLE animal ADD scientific_name VARCHAR(100);
ALTER TABLE animal ADD PRIMARY KEY(scientific_name);
ALTER TABLE animal ADD 
    FOREIGN KEY(scientific_name) 
    REFERENCES scarydatabase(scientific_name);

# `ALTER TABLE` with `DROP` removes Stuff from Tables.
ALTER TABLE animal DROP age;
ALTER TABLE animal DROP PRIMARY KEY;
ALTER TABLE animal DROP FOREIGN KEY;

{{</highlight>}}

## DML - Data Manipulation Language
### Inserting Data
### Updating Data
### Selecting Data

{{<highlight mysql "linenos=table,linenostart=35">}}

### INSERTING DATA
INSERT INTO animal(id,name,species,age,habitat_id) VALUES (1, 'Dog', 'tikkcutekollo', 2, 001);
INSERT INTO animal VALUES (2, 'Cat', 'cutekollo', 10, 001);
INSERT INTO animal SET 
    id=3,
    name='cockroach',
    species='uglykollo',
    age=1,
    habitat_id=001;

### UPDATING DATA
UPDATE animal SET species='cutekollo', age = 4 WHERE habitat_id = 001;

### DELETING DATA
DELETE FROM animal WHERE id = 1;
TRUNCATE TABLE animal;

### QUERYING DATA aka SELECTING DATA aka RETRIVING DATA
#An example of a single-table query
SELECT name,species FROM animal  
    WHERE id != 3
    GROUP BY species  
    HAVING AVG(age) > 3  
    ORDER BY AVG(age) DESC;

# Use `DISTINCT` to display only the different values among duplicates
SELECT DISTINCT name FROM animal;

## Conditions
SELECT * FROM animal WHERE species='uglykollo' AND age > 9;
SELECT * FROM animal WHERE species='cutekollo' OR habitat_id=001;
SELECT * FROM animal WHERE id NOT IN (1,2);  #`IN` is equal to multiple OR conditions
SELECT * FROM animal WHERE age BETWEEN 13 AND 18;  #to get teenage animals in the zoo XD
SELECT * FROM animal WHERE name LIKE 'S%';
SELECT * FROM animal WHERE name LIKE '%s';
SELECT * FROM animal WHERE name LIKE 'K___';
SELECT * FROM animal WHERE name NOT LIKE 'San%';

{{</highlight>}}











