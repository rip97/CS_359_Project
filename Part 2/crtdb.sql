--Creates by Al

--Creates by Justyn

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
