--Creates by Al

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
    Foreign key (videoCode) references Video(videoCode),
    Foreign key (siteCode) references Site (siteCode)
);

create table Administers(
    empId integer, 
    siteCode integer,
    Foreign key (empId) references Administrator (empId),
    Foreign key (siteCode) references Site (siteCode)
);

create table Specializes(
    empId integer, 
    modelNo text,
    Foreign key (empId) references TechnicalSupport (empId),
    Foreign key (modelNo) references Model (modelNo)
);

create table Purchases(
    clientId integer, 
    empId integer, 
    packageId integer,
    commissionRate numeric,
    Foreign key (empId) references Salesman (empId),
    Foreign key (packageId) references AirtimePackage (packageId)
);

create table Locates(
    serialNo text, 
    siteCode integer,
    Foreign key (serialNo) references DigitalDisplay (serialNo) ,
    Foreign key (siteCode) references Site (siteCode) 
);
