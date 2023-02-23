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
CREATE TABLE TechnicalSupport (
    empId INTEGER,
    name VARCHAR(40),
    gender CHAR(1),
	PRIMARY KEY (empId)
);

CREATE TABLE Administrator (
    empId INTEGER,
    name VARCHAR(40),
    gender char(1),
	PRIMARY KEY (empId)

);

CREATE TABLE Salesman (
    empId INTEGER,
    name VARCHAR(40),
    gender CHAR(1),
	PRIMARY KEY (empId)
);

CREATE TABLE AirtimePackage (
    packageId INTEGER,
    class VARCHAR(16)
		CHECK (class IN ('economy', 'whole day', 'golden hours')),
    startDate DATE,
    lastDate DATE,
    frequency INTEGER,
    videoCode INTEGER,
	PRIMARY KEY (packageId)
);

CREATE TABLE AdmWorkHours (
    empId INTEGER,
    day DATE,
    hours NUMERIC(4, 2),
    PRIMARY KEY (empId, day),
    FOREIGN KEY (empId) REFERENCES Administrator (empId)
);

--Creates by Joshua
CREATE TABLE Broadcasts (
    videoCode INTEGER,
    siteCode INTEGER,
    PRIMARY KEY (videoCode, siteCode),
    FOREIGN KEY (videoCode) REFERENCES Video (videoCode),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

CREATE TABLE Administers (
    empId INTEGER,
    siteCode INTEGER,
    PRIMARY KEY (empId, siteCode),
    FOREIGN KEY (empId) REFERENCES Administrator (empId),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

CREATE TABLE Specializes (
    empId INTEGER,
    modelNo CHAR(10),
    PRIMARY KEY (empID, modelNo),
    FOREIGN KEY (empId) REFERENCES TechnicalSupport (empId),
    FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

CREATE TABLE Purchases (
    clientId INTEGER,
    empId INTEGER,
    packageId INTEGER,
    commissionRate NUMERIC(4, 2),
    PRIMARY KEY(clientId, empID, packageId),
    FOREIGN KEY (clientId) REFERENCES Client (clientId),
    FOREIGN KEY (empId) REFERENCES Salesman (empId),
    FOREIGN KEY (packageId) REFERENCES AirtimePackage (packageId)
);

CREATE TABLE Locates (
    serialNo CHAR(10),
    siteCode INTEGER,
    PRIMARY KEY (serialNo, siteCode),
    FOREIGN KEY (serialNo) REFERENCES DigitalDisplay (serialNo),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);
