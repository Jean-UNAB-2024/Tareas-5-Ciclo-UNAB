# Entidades:
- Matricula
    - ID Matricula PK
    - ID Estudiante FK
	- ID Curso FK
    - ID PlanDeEstudio FK
    - ID EscuelaProfesional FK
    - ID Facultad FK
    - ID PeriodoAcademico FK
- Pago
    - ID Pago
    - ID Matricula FK
    - Monto
    - Fecha_Pago
    - Metodo_Pago
    - TipoDePago
- Estudiante
	- ID Estudiante PK
    - ID EscuelaProfesional FK
    - ID Facultad FK
	- Nombre
	- Apellido
	- DNI
    - correoInstitucional
    - Estado: Regular/Irregular
- Docente
    - ID Docente PK
    - Nombre
    - Apellido
    - DNI
    - Especialidad
    - correoInstitucional
    - Tipo: contratado, nombrado
- Curso
	- ID Curso PK
	- ID Estudiante FK
    - ID Docente FK
    - Créditos
    - Nombre
    - Ciclo
    - ID PlanDeEstudio FK
    - Horas_Teoria
    - Horas_Practica
- Plan de Estudio
    - ID PlanDeEstudio PK
    - ID EscuelaProfesional FK
    - AñoVigencia (2020, 2022, 2025-actual)
- Escuela Profesional
    - ID EscuelaProfesional PK
    - ID PlanDeEstudio FK
    - ID Facultad FK
- Facultad
    - ID Facultad PK
- Periodo Académico
    - ID PeriodoAcademico PK
    - Año
    - Semestre
- ProgramaciónSalones
    - ID ProgramacionSalones
	- ID Curso FK
    - ID Docente FK
    - Aula
    - Horario
- Evaluación
    - ID Evaluacion PK
	- ID Estudiante FK
    - ID PeriodoAcademico FK
	- ID Curso FK
	- TipoEvaluacion (parcial, final, practica)
	- Peso (10%, 50%, 40%)
    - Nota



# Relaciones

1. Estructura Organizativa (Jerarquía)
Estas relaciones definen la pertenencia de las unidades académicas:

Facultad (1) ---- (N) Escuela Profesional: Una facultad alberga varias escuelas.

Escuela Profesional (1) ---- (N) Plan de Estudio: Una escuela puede tener varios planes (ej. Plan 2020, Plan 2025).

Plan de Estudio (1) ---- (N) Curso: Los cursos pertenecen a una malla curricular específica.

2. Identidad del Estudiante
Escuela Profesional (1) ---- (N) Estudiante: El estudiante pertenece a una escuela. Por relación implícita, ya pertenece a la Facultad de esa escuela.

3. Proceso de Matrícula y Pagos
Estudiante (1) ---- (N) Matrícula: Un alumno genera una matrícula por cada periodo.

Periodo Académico (1) ---- (N) Matrícula: Define la vigencia temporal de la inscripción.

Matrícula (1) ---- (N) Pago: Una matrícula puede tener varios comprobantes de pago asociados.

Matrícula (1) ---- (N) Curso: (Relación de muchos a muchos, usualmente mediante una tabla intermedia Detalle_Matricula).

4. Operatividad y Cátedra (Programación)
Docente (1) ---- (N) ProgramaciónSalones: Un docente tiene asignados varios horarios/aulas.

Curso (1) ---- (N) ProgramaciónSalones: Un curso se dicta en uno o varios horarios y ambientes.

Periodo Académico (1) ---- (N) ProgramaciónSalones: La disponibilidad de aulas y docentes cambia cada semestre.

5. Rendimiento Académico
Matrícula (1) ---- (N) Evaluación: La nota debe estar amarrada a la matrícula del alumno en un curso específico para ese periodo.

Curso (1) ---- (N) Evaluación: El curso define qué se evalúa (Parcial, Final, etc.).