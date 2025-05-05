# generar_resumen_pdf.py
import os
import json
from fpdf import FPDF

def generar_resumen_pdf(student_id: str, ruta_respuestas: str = "respuestas", output_dir: str = "reportes"):
    os.makedirs(output_dir, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_title(f"Resumen de respuestas - {student_id}")
    pdf.cell(200, 10, txt=f"Resumen de respuestas del estudiante {student_id}", ln=True, align='C')
    pdf.ln(10)

    def agregar_seccion(titulo: str, contenido: str):
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(200, 10, txt=titulo, ln=True)
        pdf.set_font("Arial", size=11)
        for linea in contenido.split("\n"):
            pdf.multi_cell(0, 8, txt=linea)
        pdf.ln(5)

    # ACP
    path_acp = os.path.join(ruta_respuestas, f"respuestas_{student_id}_acp.json")
    if os.path.exists(path_acp):
        with open(path_acp) as f:
            data = json.load(f)
        agregar_seccion("Análisis de Componentes Principales (ACP)", data.get("respuesta_texto", "[Sin respuesta]"))
    else:
        agregar_seccion("Análisis de Componentes Principales (ACP)", "[No se encontró respuesta]")

    # Conceptual
    path_con = os.path.join(ruta_respuestas, f"respuestas_{student_id}_conceptual.json")
    if os.path.exists(path_con):
        with open(path_con) as f:
            data = json.load(f)
        texto = ""
        texto += "\n**Selección múltiple:**\n"
        for i, resp in enumerate(data.get("seleccion_multiple", []), 1):
            texto += f"{i}. {resp}\n"
        texto += "\n**Verdadero/Falso:**\n"
        for i, resp in enumerate(data.get("falso_verdadero", []), 6):
            texto += f"{i}. {resp}\n"
        texto += "\n**Preguntas abiertas:**\n"
        for i, resp in enumerate(data.get("abiertas", []), 9):
            texto += f"{i}. {resp}\n"
        agregar_seccion("Preguntas Conceptuales", texto)
    else:
        agregar_seccion("Preguntas Conceptuales", "[No se encontró respuesta]")

    # Archivos adjuntos
    for eje, nombre in [("CA", "ca"), ("Kernel PCA", "kpca"), ("ACM", "acm")]:
        ruta = os.path.join(ruta_respuestas, f"respuestas_{student_id}_{nombre}.pdf")
        if os.path.exists(ruta):
            agregar_seccion(eje, f"Archivo adjunto: respuestas_{student_id}_{nombre}.pdf")
        else:
            agregar_seccion(eje, "[No se encontró respuesta]")

    # Guardar
    output_path = os.path.join(output_dir, f"resumen_{student_id}.pdf")
    pdf.output(output_path)
    return output_path

# Ejemplo de uso:
# ruta_pdf = generar_resumen_pdf("A001")
# print(f"PDF generado en: {ruta_pdf}")