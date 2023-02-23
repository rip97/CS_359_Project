--Creates by Al
CREATE TABLE Video (
    videoCode INTEGER,
    videoLength INTEGER,
    PRIMARY KEY (videoCode)
);

CREATE TABLE Model (
    modelNo CHAR(10),
    width NUMERIC(6, 2),
    height NUMERIC(6, 2),
    weight NUMERIC(6, 2),
    depth NUMERIC(6, 2),
    screenSize NUMERIC(6, 2),
    PRIMARY KEY (modelNo)
);

CREATE TABLE Site (
    siteCode INTEGER,
    type VARCHAR(16)
		CHECK (type IN ('Restaurant', 'Bar')),
    address VARCHAR(100),
    phone VARCHAR(16),
    PRIMARY KEY (siteCode)
);

CREATE TABLE DigitalDisplay (
    serialNo CHAR(10),
    schedulerSystem CHAR(10)
		CHECK (schedulerSystem IN ('Random', 'Smart', 'Virtue')),
    modelNo CHAR(10),
    PRIMARY KEY (serialNo),
    FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

CREATE TABLE Client (
    clientId INTEGER,
    name VARCHAR(40),
    phone VARCHAR(16),
    address VARCHAR(100),
    PRIMARY KEY (clientId)
);

--Creates by Justyn
CREATE TABLE TechnicalSupport(empId INTEGER, name VARCHAR(40), gender char(1), PRIMARY KEY (empId)); 

CREATE TABLE Administrator(empId INTEGER, name VARCHAR(40), gender char(1), PRIMARY KEY (empId)); 

CREATE TABLE Salesman(empId INTEGER, name VARCHAR(40), gender char(1), PRIMARY KEY (empId)); 

CREATE TABLE AirtimePackage(packageId INTEGER, class varchar(16) check (class in ('economy','whole day','golden hours')), startDate date, lastDate date, 
	frequency INTEGER, videoCode INTEGER, PRIMARY KEY (packageId)); 
	
CREATE TABLE AdmWorkHours (
empId INTEGER, 
day date, hours NUMERIC (4,2), 
PRIMARY KEY (empId,day), 
FOREIGN KEY (empId) REFERENCES Administrator );

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
