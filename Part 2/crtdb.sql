--Creates by Al
CREATE TABLE Video (
    videoCode INTEGER
    , videoLength INTEGER
    , PRIMARY KEY (videoCode)
);

CREATE TABLE Model (
    modelNo TEXT
    , width NUMERIC
    , height NUMERIC
    , weight NUMERIC
    , depth NUMERIC
    , screenSize NUMERIC
    , PRIMARY KEY (modelNo)
);

CREATE TABLE Site (
    siteCode INTEGER
    , type TEXT
    , address TEXT
    , phone TEXT
    , PRIMARY KEY (siteCode)
);

CREATE TABLE DigitalDisplay (
    serialNo TEXT
    , schedulerSystem TEXT
    , modelNo TEXT
    , FORIEGN KEY (modelNo) REFERENCES Model(modelNo)
);

CREATE TABLE Client (
    clientId INTEGER
    , name TEXT
    , phone TEXT
    , address TEXT
    , PRIMARY KEY (clientId)
);

--Creates by Justyn
CREATE TABLE TechnicalSupport (empId Integer PRIMARY KEY, 
name TEXT, gender TEXT); 

CREATE TABLE Administrator (empId INTEGER PRIMARY KEY, name TEXT,gender TEXT);

CREATE TABLE Salesman (empId INTEGER PRIMARY KEY, name TEXT, gender TEXT);

CREATE TABLE AirtimePackage (packageId INTEGER PRIMARY KEY, class TEXT, gender TEXT,startDate date, 
lastDate date, frequency INTEGER, videoCode INTEGER); 

CREATE TABLE AdmWorkHours (empId INTEGER, day date, hours NUMERIC, PRIMARY KEY (empId, day),
FOREIGN KEY (empId) REFERENCES Administrator (empId) 
	ON DELETE CASCADE 
	ON UPDATE NO ACTION
); 
--Creates by Joshua
create table Broadcasts(
    videoCode integer, 
    siteCode integer,
    PRIMARY KEY (videoCode, siteCode),
    Foreign key (videoCode) references Video(videoCode),
    Foreign key (siteCode) references Site (siteCode)
);

create table Administers(
    empId integer, 
    siteCode integer,
    PRIMARY KEY (empId, siteCode),
    Foreign key (empId) references Administrator (empId),
    Foreign key (siteCode) references Site (siteCode)
);

create table Specializes(
    empId integer, 
    modelNo text,
    PRIMARY KEY (empID, modelNo),
    Foreign key (empId) references TechnicalSupport (empId),
    Foreign key (modelNo) references Model (modelNo)
);

create table Purchases(
    clientId integer, 
    empId integer, 
    packageId integer,
    commissionRate numeric,
    PRIMARY KEY(clientId, empID, packageId),
    Foreign key (empId) references Salesman (empId),
    Foreign key (packageId) references AirtimePackage (packageId)
);

create table Locates(
    serialNo text, 
    siteCode integer,
    PRIMARY KEY (serialNo, siteCode),
    Foreign key (serialNo) references DigitalDisplay (serialNo) ,
    Foreign key (siteCode) references Site (siteCode) 
);
