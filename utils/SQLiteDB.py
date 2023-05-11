import sqlite3 as sql
import pandas as pd


def createDoctorTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    # print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS doctor (
                            id integer primary key autoincrement,
                            name text not null,
                            number text not null,
                            address text not null,
                            email text not null,
                            medicalRegistrationNumber text,
                            password text not null,
                            petoRegistrationNumber text
                        );
                    """)


def createPatientTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    # print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS patient (
                            id integer primary key autoincrement,
                            name text not null,
                            number text not null,
                            address text not null,
                            email text not null,
                            password text not null,
                            petoRegistrationNumber text
                        );
                    """)


def createAppointmentTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS appointment (
                            id integer primary key autoincrement,
                            name text not null,
                            number text not null,
                            address text not null,
                            email text not null,
                            petType text not null,
                            petAge text not null,
                            date text,
                            doctorName text not null,
                            doctorNumber text not null,
                            doctorAddress text not null,
                            doctorEmail text not null
                        );
                    """)


def createLocationTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\locationData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS location (
                            id integer primary key autoincrement,
                            name text not null,
                            area text not null,
                            city text not null,
                            location text not null,
                            longitude text not null,
                            latitude text not null,
                            loc_cluster int
                        );
                    """)

def createNGOLocationTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\ngoLocationData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS ngolocation (
                            id integer primary key autoincrement,
                            name text not null,
                            area text not null,
                            city text not null,
                            location text not null,
                            longitude text not null,
                            latitude text not null,
                            loc_cluster int
                        );
                    """)


def createPetShopLocationTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\petshopLocationData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS petshoplocation (
                            id integer primary key autoincrement,
                            name text not null,
                            area text not null,
                            city text not null,
                            location text not null,
                            longitude text not null,
                            latitude text not null,
                            loc_cluster int
                        );
                    """)


def loadCsvFileToLocationTbl():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\locationData.db")
    # Create a cursor object
    curs = sqlConnection.cursor()
    # # Run create table sql query
    # curs.execute("create table if not exists studentInfo" +
    #              " (name text, gender text, age integer,course text, branch text)")
    # Load CSV data into Pandas DataFrame
    location = pd.read_csv(r'C:\Users\snehal\PycharmProjects\rasa-chatbot\recommenderSystem\doctorsList.csv')

    # Write the data to a sqlite db table
    location.to_sql('location', sqlConnection, if_exists='replace', index=False)

    # Run select sql query
    curs.execute('select * from location')

    # Fetch all records
    # as list of tuples
    records = curs.fetchall()

    # Display result
    # for row in records:
    #     # show row
    #     print(row)
    # Close connection to SQLite database
    sqlConnection.close()


def retrieveLocationData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\locationData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM location")
    loc = cur.fetchall()
    con.close()
    return loc


def retrieveLocationDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\locationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM location WHERE area='{area}'")
    loc = cur.fetchall()
    locWithCluster = []
    doctorData_accumulator = []
    # Display result
    for row in loc:
        clinicName = row[0]
        area = row[1]
        loc = row[3]
        cluster = row[6]
        cur.execute(f"SELECT * FROM location WHERE loc_cluster='{cluster}'")
        locWithCluster = cur.fetchall()
        # print("locWithCluster =", locWithCluster)
        for item in locWithCluster:
            name = item[0]
            area = item[1]
            city = item[2]
            location = item[3]
            longitude = item[4]
            latitude = item[5]
            loc_cluster = item[6]

            doctorDataDict = {"name": name, "area": area, "city": city, "location": location,
                              "longitude": longitude, "latitude": latitude, "loc_cluster": loc_cluster}
            doctorData_accumulator.append(doctorDataDict)
        # print("doctorData_accumulator =", doctorData_accumulator)
    con.close()
    return doctorData_accumulator


def retrieveClusterDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\locationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM location WHERE area='{area}'")
    loc = cur.fetchall()
    con.close()
    return loc






def loadCsvFileToNGOLocationTbl():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\ngoLocationData.db")
    # Create a cursor object
    curs = sqlConnection.cursor()
    # # Run create table sql query
    # curs.execute("create table if not exists studentInfo" +
    #              " (name text, gender text, age integer,course text, branch text)")
    # Load CSV data into Pandas DataFrame
    location = pd.read_csv(r'C:\Users\snehal\PycharmProjects\rasa-chatbot\recommenderSystem\ngo.csv')

    # Write the data to a sqlite db table
    location.to_sql('ngolocation', sqlConnection, if_exists='replace', index=False)

    # Run select sql query
    curs.execute('select * from ngolocation')

    # Fetch all records
    # as list of tuples
    records = curs.fetchall()

    # Display result
    # for row in records:
    #     # show row
    #     print(row)
    # Close connection to SQLite database
    sqlConnection.close()


def retrieveNGOLocationData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\ngoLocationData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM ngolocation")
    loc = cur.fetchall()
    con.close()
    return loc


def retrieveNGOLocationDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\ngoLocationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM ngolocation WHERE area='{area}'")
    loc = cur.fetchall()
    locWithCluster = []
    doctorData_accumulator = []
    # Display result
    for row in loc:
        clinicName = row[0]
        area = row[1]
        loc = row[3]
        cluster = row[6]
        cur.execute(f"SELECT * FROM ngolocation WHERE loc_cluster='{cluster}'")
        locWithCluster = cur.fetchall()
        # print("locWithCluster =", locWithCluster)
        for item in locWithCluster:
            name = item[0]
            area = item[1]
            city = item[2]
            location = item[3]
            longitude = item[4]
            latitude = item[5]
            loc_cluster = item[6]

            doctorDataDict = {"name": name, "area": area, "city": city, "location": location,
                              "longitude": longitude, "latitude": latitude, "loc_cluster": loc_cluster}
            doctorData_accumulator.append(doctorDataDict)
        # print("doctorData_accumulator =", doctorData_accumulator)
    con.close()
    return doctorData_accumulator


def retrieveNGOClusterDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\ngoLocationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM ngolocation WHERE area='{area}'")
    loc = cur.fetchall()
    con.close()
    return loc











def loadCsvFileToPetShopLocationTbl():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\petshopLocationData.db")
    # Create a cursor object
    curs = sqlConnection.cursor()
    # # Run create table sql query
    # curs.execute("create table if not exists studentInfo" +
    #              " (name text, gender text, age integer,course text, branch text)")
    # Load CSV data into Pandas DataFrame
    location = pd.read_csv(r'C:\Users\snehal\PycharmProjects\rasa-chatbot\recommenderSystem\petShop.csv')

    # Write the data to a sqlite db table
    location.to_sql('petshoplocation', sqlConnection, if_exists='replace', index=False)

    # Run select sql query
    curs.execute('select * from petshoplocation')

    # Fetch all records
    # as list of tuples
    records = curs.fetchall()

    # Display result
    # for row in records:
    #     # show row
    #     print(row)
    # Close connection to SQLite database
    sqlConnection.close()


def retrievePetShopLocationData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\petshopLocationData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM petshoplocation")
    loc = cur.fetchall()
    con.close()
    return loc


def retrievePetShopLocationDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\petshopLocationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM petshoplocation WHERE area='{area}'")
    loc = cur.fetchall()
    locWithCluster = []
    doctorData_accumulator = []
    # Display result
    for row in loc:
        clinicName = row[0]
        area = row[1]
        loc = row[3]
        cluster = row[6]
        cur.execute(f"SELECT * FROM petshoplocation WHERE loc_cluster='{cluster}'")
        locWithCluster = cur.fetchall()
        # print("locWithCluster =", locWithCluster)
        for item in locWithCluster:
            name = item[0]
            area = item[1]
            city = item[2]
            location = item[3]
            longitude = item[4]
            latitude = item[5]
            loc_cluster = item[6]

            doctorDataDict = {"name": name, "area": area, "city": city, "location": location,
                              "longitude": longitude, "latitude": latitude, "loc_cluster": loc_cluster}
            doctorData_accumulator.append(doctorDataDict)
        # print("doctorData_accumulator =", doctorData_accumulator)
    con.close()
    return doctorData_accumulator


def retrievePetShopClusterDataWithArea(area):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\petshopLocationData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM petshoplocation WHERE area='{area}'")
    loc = cur.fetchall()
    con.close()
    return loc






# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())


def insertDoctorData(name, number, address, email, medicalRegistrationNumber, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO doctor (name, number, address, email, medicalRegistrationNumber, password) VALUES (?,?,?,?,?,?)",
        (name, number, address, email, medicalRegistrationNumber, password))
    con.commit()
    con.close()


def insertPatientData(name, number, address, email, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO patient (name, number, address, email, password) VALUES (?,?,?,?,?)",
                (name, number, address, email, password))
    con.commit()
    con.close()


def insertAllAppointmentData(name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress,
                          doctorEmail):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO appointment (name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress, doctorEmail) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress, doctorEmail))
    con.commit()
    con.close()


def insertAppointmentData(name, number, address, email, petType, petAge, date, doctorName):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO appointment (name, number, address, email, petType, petAge, date, doctorName) VALUES (?,?,?,?,?,?,?,?)",
        (name, number, address, email, petType, petAge, date, doctorName))
    con.commit()
    con.close()


def retrieveDoctorData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM doctor")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveAppointmentData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM appointment")
    appointmentData = cur.fetchall()
    # print("appointmentData = ", appointmentData)
    con.close()
    return appointmentData


def retrieveDoctorDataWithName(name):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM doctor WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientDataWithName(name):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM patient WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveDoctorDataWithEmail(email):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM doctor WHERE email='{email}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientDataWithEmail(email):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM patient WHERE email='{email}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def showAllTables():
    try:
        # Making a connection between sqlite3
        # database and Python Program
        # sqliteConnection = sql.connect(r'C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db')
        # sqliteConnection = sql.connect(r'C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db')
        sqliteConnection = sql.connect(
            r'C:\Users\snehal\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db')
        print("Connected to SQLite")

        # Getting all tables from sqlite_master
        sql_query = """SELECT name FROM sqlite_master
        WHERE type='table';"""

        # Creating cursor object using connection object
        cursor = sqliteConnection.cursor()

        # executing our sql query
        cursor.execute(sql_query)
        print("List of tables\n")

        # printing all tables list
        # print(cursor.fetchall())

    except sql.Error as error:
        print("Failed to execute the above query", error)

    finally:

        # Inside Finally Block, If connection is
        # open, we need to close it
        if sqliteConnection:
            # using close() method, we will close
            # the connection
            sqliteConnection.close()

            # After closing connection object, we
            # will print "the sqlite connection is
            # closed"
            print("the sqlite connection is closed")


# createPatientTableIfNotExist()
# createDoctorTableIfNotExist()
# createAppointmentTableIfNotExist()
# retrieveDoctorDataWithEmail("st@gmail.com")
# createTableIfNotExist()
# showAllTables()
# createLocationTableIfNotExist()
# loadCsvFileToLocationTbl()
# retrieveAppointmentData()
# print(retrieveLocationData())
# print(retrieveLocationDataWithArea("Mankapur"))
# print(retrieveLocationDataWithArea("Laxmi Nagar"))

# createNGOLocationTableIfNotExist()
# loadCsvFileToNGOLocationTbl()
# retrieveAppointmentData()
# print(retrieveNGOLocationData())
# print(retrieveNGOLocationDataWithArea("Mankapur"))

# createPetShopLocationTableIfNotExist()
# loadCsvFileToPetShopLocationTbl()
# retrieveAppointmentData()
# print(retrievePetShopLocationData())
# print(retrievePetShopLocationDataWithArea("Mankapur"))