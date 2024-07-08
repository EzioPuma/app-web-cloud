import pymysql

db_host = 'db-veterinaria.cjuee6yaqisf.us-west-2.rds.amazonaws.com'
db_user = 'brian'
db_password = '12345612345'
db_database = 'dbveterinaria'
db_table = 'servicios'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        return connection_sql
    except Exception as err:
        print("Error connecting to the database")
        print(err)
        return None

def add_service(nombremascota, tiposervicio, nombredueno, telefonodueno, comentarios):
    instruction_sql = f"""
    INSERT INTO {db_table} (nombremascota, tiposervicio, nombredueno, telefonodueno, comentarios)
    VALUES (%s, %s, %s, %s, %s)
    """
    connection_sql = connectionSQL()
    try:
        if connection_sql is not None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql, (nombremascota, tiposervicio, nombredueno, telefonodueno, comentarios))
            connection_sql.commit()
            service_id = cursor.lastrowid  # Obtén el ID del registro insertado
            print("Service added with ID:", service_id)
            return service_id  # Retorna el ID del servicio añadido
        else:
            print("Error connecting to the database")
            return None
    except Exception as err:
        print("Error adding the service")
        print(err)
        return None


def consult_service(idservicio):
    instruction_sql = f"SELECT * FROM {db_table} WHERE idservicio = %s"
    connection_sql = connectionSQL()
    try:
        cursor = connection_sql.cursor()
        cursor.execute(instruction_sql, (idservicio,))
        result_data = cursor.fetchall()
        return result_data
    except Exception as err:
        print("Error", err)
        return False