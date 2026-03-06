from fastapi import APIRouter, HTTPException
from app.vista.vista import PacienteVista
from app.models.queries import PacienteModel

router = APIRouter()


@router.post("/pacientes/")
def crear_paciente(paciente: PacienteVista):
    paciente_id = PacienteModel.crear(paciente)
    return {"message": "Paciente registrado", "id": paciente_id}

@router.get("/pacientes/")
def obtener_pacientes():
    return PacienteModel.listar_todos()


@router.put("/pacientes/{id_paciente}")
def actualizar_paciente(id_paciente: int, paciente: PacienteVista):
    PacienteModel.actualizar(id_paciente, paciente)
    return {"message": "Paciente actualizado"}


@router.delete("/pacientes/{id_paciente}")
def eliminar_paciente(id_paciente: int):
    PacienteModel.eliminar(id_paciente)
    return {"message": "Paciente eliminado"}