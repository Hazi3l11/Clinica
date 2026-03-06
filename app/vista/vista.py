from pydantic import BaseModel
from typing import Optional
from datetime import date


class PacienteVista(BaseModel):
    nombre: str
    edad: int
    telefono: Optional[str] = None
    direccion: Optional[str] = None


class CitaVista(BaseModel):
    id_paciente: int
    fecha_cita: date
    motivo: Optional[str] = None
    proxima_cita: Optional[date] = None


class RecetaVista(BaseModel):
    id_cita: int
    medicamento: str
    dosis: str
    indicaciones: Optional[str] = None