import sys
import sqlite3

#main function
def main():
    query = getQuery()
    queryResult = runQuery(query)
    print(type(queryResult))
    print (queryResult)

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
    if(num == 1):
        return f"SELECT * FROM Site where address like '%{where}%'"
    #TODO: write other queries

    return ""

# runs the query provided and returns the query results as a tuple, whith element 0 being the table columns and element 1 being the query results as a list.
# here is what query 1 results look like if an empty string is passed in the where statement:
#(['siteCode', 'type', 'address', 'phone'], [(1, 'Restaurant', '123 Spring Road Albuquerque New Mexico 87101', '5058561111'), (2, 'Bar', '1023 East Main Albuquerque New Mexico 87101', '5054501010'), (3, 'Bar', '10023 Rocky Road Albuquerque New Mexico 87101', '5057801001'), (4, 'Restaurant', '111 Main Albuquerque New Mexico 87101', '5053512000'), (5, 'Bar', '1010 Cypress Road Albuquerque New Mexico 87101', '5056549000')]) 
def runQuery(query):
    result = []
    column_names = []
    try:
        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('abc.sqlite')
        cursor = sqliteConnection.cursor()
        
        # Write a query and execute it with cursor
        cursor.execute(query)
        column_names = [i[0] for i in cursor.description]
        # Fetch and output result
        result = cursor.fetchall()
        # print(result)
    
        # Close the cursor
        cursor.close()
 
    # Handle errors
    except sqlite3.Error as error:
        print('Error occurred - ', error)
 
    # Close DB Connection irrespective of success
    # or failure
    finally:
    
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite Connection closed')
    return (column_names,result)

# runs the main function
main()
