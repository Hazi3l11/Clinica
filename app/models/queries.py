from app.db.database import get_db_connection

class PacienteModel:

    @staticmethod
    def crear(paciente):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO pacientes (nombre, edad, telefono, direccion)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (
            paciente.nombre,
            paciente.edad,
            paciente.telefono,
            paciente.direccion
        ))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener_por_id(id_paciente):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id_paciente,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def actualizar(id_paciente, paciente):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        UPDATE pacientes
        SET nombre=%s, edad=%s, telefono=%s, direccion=%s
        WHERE id_paciente=%s
        """
        cursor.execute(query, (
            paciente.nombre,
            paciente.edad,
            paciente.telefono,
            paciente.direccion,
            id_paciente
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_paciente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pacientes WHERE id_paciente=%s", (id_paciente,))
        conn.commit()
        conn.close()