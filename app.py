from flask import Flask, request, make_response
import mysql.connector


app = Flask(__name__)

cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
#@app.route("/")
#def home():
#    return "Home"
#works now once the port changed from 6000 to 6001


# This should return all the customers in the following format.

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
        cursor = cnx.cursor()
        cursor.execute('SELECT * from customers')
        customer_list = []
        for customer_id, gender, age, annualincome, spendingscore, profession, workexp, familysize in cursor:
            customer = {}
            customer['CustomerID'] = customer_id
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annualincome
            customer['SpendingScore'] = spendingscore
            customer['Profession'] = profession
            customer['WorkExperience'] = workexp
            customer['FamilySize'] = familysize
            customer_list.append(customer)
        cursor.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
# This should return a shopper with the specified id. If no shopper is found
# an appropriate error message should be returned

@app.route('/customer/<customer_id>', methods=['GET'])
def get_sudent(customer_id):
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * from customers WHERE CustomerID={customer_id}")
        row = cursor.fetchone()
        customer = {}
        if row is not None:
            customer_id, gender, age, annualincome, spendingscore, profession, workexp, familysize = row
            customer['CustomerID'] = customer_id
            customer['Gender'] = gender
            customer['Age'] = age
            customer['AnnualIncome'] = annualincome
            customer['SpendingScore'] = spendingscore
            customer['Profession'] = profession
            customer['WorkExperience'] = workexp
            customer['FamilySize'] = familysize
            cursor.close()
            return make_response(customer, 200)
        else:
            return make_response({'error': 'Student not found'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)

# This should allow a shopper to be added to the database. The endpoint
# should accept a body in the following format. An appropriate success
# message should be returned

@app.route('/add_customer', methods=['POST'])
def add_student():
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                    host='127.0.0.1',
                                    database='lab3')
        cursor = cnx.cursor()
        content = request.json
        id = content['CustomerID']
        gender = content['Gender']
        age = content['Age']
        annualincome = content['AnnualIncome']
        spendingscore = content['SpendingScore']
        profession = content['Profession']
        WorkExperience = content['WorkExperience']
        FamilySize = content['FamilySize']
        cursor.execute(f"INSERT INTO customers VALUES({id},'{gender}',{age},{annualincome},{spendingscore},'{profession}', {WorkExperience}, {FamilySize})")
        cnx.commit()
        cursor.close()
        return make_response({"success" : "Student added"}, 201)
    except Exception as e:
        print(e)
        return make_response({'error': 'An error has occured'}, 400)

# This should allow a customer’s profession to be added with the specified
# customer id. The endpoint should accept a body with the following format.
# An appropriate success message should be shown.

@app.route('/update_profession/<customer_id>', methods=['PUT'])
def update_address(customer_id):
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                        host='127.0.0.1',
                                        database='lab3')
        cursor = cnx.cursor()
        content = request.json
        profession = content['Profession']
        cursor.execute(f"UPDATE Customers SET Profession= '{profession}' WHERE CustomerID={customer_id}")
        #print(f"UPDATE Customers SET AnnualIncome={annualincome} WHERE CustomerID={customer_id}")
        cnx.commit()
        cursor.close()
        return make_response({"success" : "Student updated"}, 202)
    except Exception as e:
       return make_response({'error': str(e)}, 400)

# This should return a report with the highest income earners by profession.

@app.route('/highest_income_report', methods=['GET'])
def get_highest_income_earners():
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
        cursor = cnx.cursor()
        cursor.execute('SELECT customerid, profession, annualincome from customers group by customerid, profession, annualincome order by annualincome desc')
        customer_list = []
        for customer_id, annualincome,profession in cursor:
            customer = {}
            customer['CustomerID'] = customer_id
            customer['AnnualIncome'] = annualincome
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

# This should show the total income earned by profession

@app.route('/total_income_report', methods=['GET'])
def get_total_income_report():
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
        cursor = cnx.cursor()
        cursor.execute('SELECT profession, sum(annualincome) as totalincome from customers group by profession order by totalincome desc')
        customer_list = []
        for profession, totalincome in cursor:
            customer = {}
            customer['TotalIncome'] = totalincome
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

# This should show the average work experience by profession for
# customers that are young high earners. A young high earner is one which
# makes over $50,000 and is younger than 35 years old.


@app.route('/average_work_experience', methods=['GET'])
def get_average_work_experience():
    try:
        cnx = mysql.connector.connect(user='jordan', password='Firekid109',
                                host='127.0.0.1',
                                database='lab3')
        cursor = cnx.cursor()
        cursor.execute('SELECT profession, avg(workexperience) as AverageExperience from  customers where annualincome > 50000 and age < 35 group by profession')
        customer_list = []
        for profession, avgworkexperience in cursor:
            customer = {}
            customer['Average_Work_Experience'] = avgworkexperience
            customer['Profession'] = profession
            customer_list.append(customer)
        cursor.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

# This should show the average spending score by gender for the profession
# specified. E.g. /average_spending_score/engineers would return the average
# spending score by gender for engineers.
@app.route('/average_spending_score/<profession>', methods=['GET'])
def get_average_spending_score(profession):
    try:
        cursor = cnx.cursor()
        cursor.execute(f"select gender, avg(spendingscore) as averagespendingscore from customers where profession = '{profession}' group by gender")
        customer_list = []
        for gender, avgspendingscore in cursor:
            customer = {}
            customer['Average_Spending_Score'] = avgspendingscore
            customer['Gender'] = gender
            customer_list.append(customer)
        cursor.close()
        return make_response(customer_list, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)




if __name__ == '__main__':
    app.run(debug = True,port=3000) #debug allows edits to be done live on the server and it updates
    #note well- adjust port until it works (works on my computer)