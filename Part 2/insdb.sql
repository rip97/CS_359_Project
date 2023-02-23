--This file is used to insert data into tables created in the crtdb.sql file.

--Al's inserts
INSERT INTO VIDEO 
VALUES (1, 5)
	, (2, 10)
	, (3, 15)
	, (4, 20)
	, (5, 25)
GO

INSERT INTO Model
VALUES ('MN1000', 10.0, 12.0, 55.0, 3.5, 65.0)
	, ('MN1001', 8.0, 10.0, 45.0, 6.5, 48.0)	
	, ('MN1003', 12.0, 15.0, 60.0, 1.5, 72.0)
	, ('MN1004', 6.0, 8.0, 35.0, 6.5, 32.0)
	, ('MN1005', 15.0, 20.0, 65.0, 2.5, 60.0)
GO


INSERT INTO Site
VALUES (1, 'Restaurant', '123 Spring Road Albuquerque New Mexico 87101', '5058561111')
	, (2, 'Bar', '1023 East Main Albuquerque New Mexico 87101', '5054501010')
	, (3, 'Bar', '10023 Rocky Road Albuquerque New Mexico 87101', '5057801001')
	, (4, 'Restaurant', '111 Main Albuquerque New Mexico 87101', '5053512000')
	, (5, 'Bar', '1010 Cypress Road Albuquerque New Mexico 87101', '5056549000')
GO


INSERT INTO DigitalDisplay
VALUES ('SN1001', 'Random', 'MN1000')
	, ('SN1002', 'Smart', 'MN1001')
	, ('SN1003', 'Random', 'MN1004')
	, ('SN1004', 'Virtue', 'MN1005')
	, ('SN1005', 'Smart', 'MN1003')
GO

INSERT INTO Client 
VALUES (1, 'John Doe', '5057895050', '10 East Broadway Albuquerque New Mexico 87101')
	, (2, 'Allen James', '6018558801', '651 University Ave Albuquerque New Mexico 87101')
	, (3, 'Matt Johnson', '3109914545', '9900 Juniper Street Albuquerque New Mexico 87101')
	, (4, 'Edna Polk', '5054589800', '1880 Montgomery Ave Albuquerque New Mexico 87101')
	, (5, 'Bill Thomas', '7208756548', '6000 Central Ave Albuquerque New Mexico 87101')
GO

--Justyn's inserts
INSERT INTO TechnicalSupport VALUES 
(1001,'Bruce Evans', 'M'),
(1002,'Anahi Booker','F'),
(1003,'Seth Evans','M'),
(1004,'Caylee Hart','F'),
(1005,'Javier Baxter','M') 
GO 

INSERT INTO Administrator VALUES
(2010,'Miracle Cummings','F'),
(2011,'Abdiel Castillo','F'),
(2012,'Camila Anthony','F'),
(2013,'Howard Richard','M'),
(2014,'Dominik Potts','M')

GO 

INSERT INTO Salesman VALUES 
(3100,'Nikolai Valencia','M'),
(3105,'Jack Bonilla','M'),
(3110,'Mireya Golden','F'),
(3115,'Tiara Copeland','F'),
(3120,'Jaylynn Calderon','F')

GO 

INSERT INTO AirtimePackage 
VALUES 
	(2102,'golden hours',2023-03-01,2023-04-01,4,100012)
	,(2104,'whole day',2023-03-01,2023-05-06,2,100022) 
	,(2106,'economy',2023-01-01,2023-12-31,10,100032)
	,(2108,'golden hours',2023-04-01,2023-04-31,2,100042)
	,(2110,'whole day',2023-03-01,2023-03-02,1,100052)
	

--Joshua's inserts
