import sqlite3 as sql


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

# createPatientTableIfNotExist()
# createDoctorTableIfNotExist()
# retrieveDoctorDataWithEmail("st@gmail.com")
# createTableIfNotExist()
#
# insertRecipeData("python", pythonData)
# print(retrieveCorpusData())
# print(retrieveCorpusDataWithItemName("python"))
