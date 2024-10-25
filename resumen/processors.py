import os
from typing import Tuple, Optional
from .pdf_handler import ManipuladorPDF
from .openai_client import EnviadorOpenAI

def procesar_articulos(directorio_raiz: str, modelo_openai: str, prompt_estandar: list):
    enviador = EnviadorOpenAI(modelo=modelo_openai)
    print("Carpetas encontradas:", os.listdir(directorio_raiz))
    for carpeta in os.listdir(directorio_raiz):
        ruta_carpeta = os.path.join(directorio_raiz, carpeta)
        if os.path.isdir(ruta_carpeta):
            print(f"Procesando carpeta: {carpeta}")
            
            carpeta_respuestas = os.path.join(ruta_carpeta, "respuestas")
            os.makedirs(carpeta_respuestas, exist_ok=True)
            
            for archivo in os.listdir(ruta_carpeta):
                if archivo.lower().endswith('.pdf'):
                    ruta_pdf = os.path.join(ruta_carpeta, archivo)
                    print(f"  Extrayendo texto de: {archivo}")
                    try:
                        manipulador = ManipuladorPDF(ruta_pdf)
                        texto = manipulador.extraer_texto_simple()
                        print(f"  Enviando texto a OpenAI para: {archivo}")
                        respuesta, tokens_enviados, tokens_recibidos, tokens_totales = enviador.enviar_texto(texto, prompt_estandar)
                        print(f"Tokens enviados: {tokens_enviados} Tokens recibidos: {tokens_recibidos} Tokens totales: {tokens_totales}")
                        
                        ruta_respuesta = os.path.join(carpeta_respuestas, f"{os.path.splitext(archivo)[0]}_respuesta.txt")
                        with open(ruta_respuesta, 'w', encoding='utf-8') as f:
                            f.write(respuesta)
                        print(f"  Respuesta guardada en: {ruta_respuesta}")
                    except Exception as e:
                        print(f"  Error procesando {archivo}: {e}")

def combinar_archivos_txt(ruta_carpeta: str) -> str:
    contenido_combinado = ""
    
    if not os.path.isdir(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' no existe.")
        return contenido_combinado
    
    for archivo in os.listdir(ruta_carpeta):
        if archivo.lower().endswith('.txt'):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            nombre_archivo = os.path.splitext(archivo)[0]
            
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    contenido_combinado += f"Titulo del archivo: {nombre_archivo}\n\nTexto:\n\n{contenido}\n\n"
            except Exception as e:
                print(f"Error al leer el archivo '{archivo}': {str(e)}")
    
    return contenido_combinado

def generar_resumen_final(ruta_carpeta: str, modelo_openai: str, prompt_estandar: list) -> Tuple[Optional[str], int, int, int]:
    texto_combinado = combinar_archivos_txt(ruta_carpeta)
    enviador = EnviadorOpenAI(modelo=modelo_openai)
    respuesta, tokens_enviados, tokens_recibidos, tokens_totales = enviador.enviar_texto(texto_combinado, prompt_estandar)
   
    if respuesta:
        print("Respuesta obtenida:")
        print(respuesta)
        print(f"Tokens enviados: {tokens_enviados}")
        print(f"Tokens recibidos: {tokens_recibidos}")
        print(f"Tokens totales: {tokens_totales}")
        
        ruta_respuesta = os.path.join(os.path.dirname(ruta_carpeta), "respuesta_final.txt")
        with open(ruta_respuesta, 'w', encoding='utf-8') as f:
            f.write(respuesta)
        print(f"Respuesta guardada en: {ruta_respuesta}")
    
    return respuesta, tokens_enviados, tokens_recibidos, tokens_totales

