from pprint import pprint
import sys
import sqlite3


#main function
def main():
    query = getQuery()
    queryResult = runQuery(query)

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
            return sys.argv[2]
    return ""

#get the query to be ran depending on argument(s) passed from command line.
def getQuery():
    num = getQuestionNumFromParams() #param arg[1]
    where = getWhereValueFromParams(num) #param arg[2], if expected

    match num:
        case 1:
            return f"SELECT * FROM Site where address like '%{where}%'"
        case 2: 
            return f"SELECT 'Case 2'"
        case 3: 
            return f"SELECT 'Case 3'"
        case 4: 
            return f"SELECT 'Case 4'"
        case 5:            
            return (f"SELECT adm.empId, adm.name, hrs.hours " 
                    f"FROM Administrator adm "
                    f"INNER JOIN AdmWorkHours hrs "
                    f"ON hrs.empId = adm.empId "
                    f"ORDER BY hrs.hours"
                    )
        case 6: 
            return f"SELECT 'Case 6'"
        case 7: 
            return f"SELECT 'Case 7'"
        case 8: 
            return f"SELECT 'Case 8'"
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
def runQuery(query):
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
            cursor.execute(query)
            column_names = [i[0] for i in cursor.description]        

            ## Fetch and output result
            result = cursor.fetchall()

            pprint(column_names, width=125)
            pprint(result, width=125)

            # Close the cursor
            cursor.close()
    


       ##Iterate over elements to determine the max width
       #FINAL LENGTH IS STILL TOO SMALL, SET DEFAULT TO 125 chars
       #WILL NEED TO REMOVE FROM FINAL REPO
       # maxLength = 0
       # elemSum = 0
       # for elem in result:
       #     tempSum = 0
       #     for j in elem:
       #         if type(j) == int:
       #             tempSum += j
       #             elemSum += j
       #             print("Value of J: ", j)
       #             print("Int Value: ", tempSum)
       #         else:
       #             tempSum += len(j)
       #             print("Non-int length: ", len(j))
       #             print("new Sum Value: ", tempSum)              
       #     print("tempSum: ", tempSum)
       #     print("ElemSum: ", elemSum)
       #     if tempSum > elemSum:
       #         elemSum = tempSum
       # if elemSum > maxLength:
       #     maxLength = elemSum

       # print("Max Width: ", maxLength)
       # pprint(column_names, width=maxLength)
       # pprint(result, width=maxLength)
      
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
    
    #returns column names and results in a single line. 
    #TODO: Look into formatting rather than just running print(column_names) above
    #look into iterating over result list and pulling max length of element and use
    #that as the width in the pprint width parameter
    return (column_names,result) 

    #return ""

# runs the main function
main()
