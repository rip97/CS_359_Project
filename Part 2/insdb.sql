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
	, (3, 'Bar', '123 Spring Road Albuquerque New Mexico 87101', '5058561111')
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

--Joshua's inserts
