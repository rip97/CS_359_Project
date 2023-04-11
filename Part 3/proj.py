from pprint import pprint
import sys
import sqlite3


#main function
def main():
    query = getQuery() #query string
    where = getWhereValueFromParams(getQuestionNumFromParams()) #query parameters, if any
    queryResult = runQuery(query, where)

# Helper to quickly identify what questions expect a where clause
def doesQuestionContainWhereClause(num):
    if(num == 1 or num == 2 or num == 4 or num == 6):
        return True
    return False

# gets the question number to be ran from the command line parameter(s) passed
def getQuestionNumFromParams():
    # Check if there is an argument passed to the program
    if len(sys.argv) > 1:
        # The first argument is the name of the script
        # The second argument (index 1) is the input parameter
        return int(sys.argv[1])
    else:
        return 0

# gets the where parameter of the query based on the question number from the command line parameters. 
def getWhereValueFromParams(num):
    if(doesQuestionContainWhereClause(num)):
        if len(sys.argv) > 2:
            # The first argument is the name of the script
            # The second argument (index 1) is the input parameter
            if(num == 1) :
                return (f"%{sys.argv[2]}%",) #the only query that is using a like statement is query number 1. Our like statement requires param to be surrounded by % 
            else:
                return (sys.argv[2],)
    return ""

#get the query to be ran depending on argument(s) passed from command line.
def getQuery():
    num = getQuestionNumFromParams() #param arg[1]

    match num:
        case 1:
            return f"SELECT * FROM Site where address like ?"
        case 2: 
            return (f"SELECT DD.serialNo, DD.modelNo, TS.Name FROM DigitalDisplay as DD " 
                    f"INNER JOIN Specializes as S ON S.modelNo = DD.modelNo "
                    f"INNER JOIN TechnicalSupport as TS ON TS.empId = S.empId "
                    f"WHERE dd.schedulerSystem = ?"
                    )
        case 3: 
            return (f"SELECT "
                    f"SUBSTR(name, 0, INSTR(name, ' ')) as NAME, "
                    f"COUNT(*) as CNT, "
                    f"CASE "
                    f"WHEN COUNT(*) > 1 "
                    f"  THEN "
                    f"    (SELECT group_concat(( '(' || empId || ',' || name || ',' || gender || ')'), ', ')  FROM Salesman "
                    f"      GROUP BY SUBSTR(name, 0, INSTR(name, ' ')) "
                    f"HAVING COUNT(*) > 1) "
                    f"END '' "
                    f"FROM Salesman " 
                    f"GROUP by SUBSTR(name, 0, INSTR(name, ' '))"       
                   )
        case 4: 
            return (f"SELECT name, address FROM Client "
                    f"WHERE phone  = ? "
                    )
        case 5:            
            return (f"SELECT adm.empId, adm.name, hrs.hours " 
                    f"FROM Administrator adm "
                    f"INNER JOIN AdmWorkHours hrs "
                    f"ON hrs.empId = adm.empId "
                    f"ORDER BY hrs.hours"
                    )
        case 6: 
            return (f"SELECT ts.name "
                    f"FROM TechnicalSupport ts "
                    f"INNER JOIN Specializes s "
                    f"ON s.empId = ts.empId "
                    f"INNER JOIN Model m "
                    f"ON m.modelNo = s.modelNo "
                    f"WHERE m.modelNo = ? "
                    )

        case 7: 
            return (f"SELECT s.name, p.avgRate as AverageCommissionRate "
                    f"FROM Salesman s "
                    f"INNER JOIN (SELECT p.empId, AVG(p.commissionRate) as avgRate "
                    f"FROM Purchases p "
                    f"GROUP BY p.empId "
                    f") p "
                    f"ON p.empId = s.empId "
                    f"ORDER BY p.avgRate DESC"
                    )
        case 8: 
            return (f"SELECT 'Administrator' as Role, COUNT(*) as cnt FROM Administrator "
                    f"UNION "
                    f"SELECT 'Salesman', COUNT(*) FROM Salesman "
                    f"UNION "
                    f"SELECT 'Technicians', COUNT(*) FROM TechnicalSupport "
                    )
        case _: # Default Case
            return f"'Invalid Parameter'"

    return ""

# runs the query provided and returns the query results as a tuple, whith element 0 being 
# the table columns and element 1 being the query results as a list.
# here is what query 1 results look like if an empty string is passed in the where statement:
#(['siteCode', 'type', 'address', 'phone'], 
#[(1, 'Restaurant', '123 Spring Road Albuquerque New Mexico 87101', '5058561111'), 
#(2, 'Bar', '1023 East Main Albuquerque New Mexico 87101', '5054501010'), 
#(3, 'Bar', '10023 Rocky Road Albuquerque New Mexico 87101', '5057801001'), 
#(4, 'Restaurant', '111 Main Albuquerque New Mexico 87101', '5053512000'), 
#(5, 'Bar', '1010 Cypress Road Albuquerque New Mexico 87101', '5056549000')]) 
def runQuery(query, args):
    result = []
    column_names = []
    try:

        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('abc.sqlite')
        
        #If invalid parameter entered return error, otherwise execute query
        if 'Invalid' in query:
            print("Invalid Parameter: Please enter a number between 1 and 8.")
        else:
            cursor = sqliteConnection.cursor()
            ## Write a query and execute it with cursor
            cursor.execute(query,args)
            column_names = [i[0] for i in cursor.description]        

            ## Fetch and output result
            result = cursor.fetchall()

            pprint(column_names, width=125)
            pprint(result, width=125)

            # Close the cursor
            cursor.close()
      
    # Handle errors and return error line
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        print("Line Number {}".format(sys.exc_info()[-1].tb_lineno))
 
    # Close DB Connection irrespective of success
    # or failure
    finally:
    
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite Connection closed')
    
    return (column_names,result) 


# runs the main function
main()
