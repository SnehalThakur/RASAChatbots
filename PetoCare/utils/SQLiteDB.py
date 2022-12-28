import sqlite3 as sql


DOCTORS_LIST = {
    "/DrYogitaGame":
        {
            "doctorName": "Dr. Yogita Game",
            "doctorNumber": "8669416075",
            "doctorAddress": "Near Alankar Cinema, North Ambazari Road, S Ambazari Rd, Dharampeth, Nagpur, Maharashtra 440010",
            "doctorEmail": "rbry-mqwu",
            "experience": "5"
        },
    "/DrKaislashMarwah":
        {
            "doctorName": "Dr. Kailash Marwah",
            "doctorNumber": "9421887656",
            "doctorAddress": "Mandar Flats, N Bazar Rd, Shivaji Nagar, Nagpur, Maharashtra 440010",
            "doctorEmail": "rbry-mqwu",
            "experience": "7"
        },
    "/DrRushikeshDhote":
        {
            "doctorName": "Dr. Rushikesh Dhote",
            "doctorNumber": "8530426407",
            "doctorAddress": "B/No. 77, Matoshree, Lane 4, Katol Rd, KT Nagar, Nagpur, Maharashtra 440013",
            "doctorEmail": "rbry-mqwu",
            "experience": "10"
        },
    "/DrPrabhuRaut":
        {
            "doctorName": "Dr. Prabhu Raut",
            "doctorNumber": "7620695473",
            "doctorAddress": "52GW+X7F, Katol Road, Friends Colony, beside State Bank Of Indian, Nagpur, Maharashtra 440013",
            "doctorEmail": "rbry-mqwu",
            "experience": "8"
        }
}


def createDoctorTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS doctor (
                            id integer primary key autoincrement,
                            name text not null,
                            number text not null,
                            address text not null,
                            email text not null,
                            medicalRegistrationNumber text not null,
                            password text not null,
                            petoRegistrationNumber text
                        );
                    """)


def createPatientTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    print(sqlConnection)

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
    sqlConnection = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
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


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())


def insertDoctorData(name, number, address, email, medicalRegistrationNumber, password):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO doctor (name, number, address, email, medicalRegistrationNumber, password) VALUES (?,?,?,?,?,?)",
                (name, number, address, email, medicalRegistrationNumber, password))
    con.commit()
    con.close()


def insertPatientData(name, number, address, email, password):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO patient (name, number, address, email, password) VALUES (?,?,?,?,?)",
                (name, number, address, email, password))
    con.commit()
    con.close()


def insertAppointmentData(name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress, doctorEmail):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO appointment (name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress, doctorEmail) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (name, number, address, email, petType, petAge, date, doctorName, doctorNumber, doctorAddress, doctorEmail))
    con.commit()
    con.close()


def retrieveDoctorData():
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM doctor")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientData():
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveAppointmentData():
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM appointment")
    appointmentData = cur.fetchall()
    print("appointmentData = ",appointmentData)
    con.close()
    return appointmentData


def retrieveDoctorDataWithName(name):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM doctor WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientDataWithName(name):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM patient WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveDoctorDataWithEmail(email):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM doctor WHERE email='{email}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrievePatientDataWithEmail(email):
    con = sql.connect(r"C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM patient WHERE email='{email}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def showAllTables():
    try:
        # Making a connection between sqlite3
        # database and Python Program
        # sqliteConnection = sql.connect(r'C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\patientData.db')
        # sqliteConnection = sql.connect(r'C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\doctorData.db')
        sqliteConnection = sql.connect(r'C:\Users\Snehal Thakur\PycharmProjects\rasa-chatbot\utils\SQLiteDB\appointmentData.db')
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
        print(cursor.fetchall())

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
# retrieveAppointmentData()
