import os
from pypdf import PdfReader

class ManipuladorPDF:
    def __init__(self, ruta_archivo: str):
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe.")
        
        try:
            self.reader = PdfReader(ruta_archivo)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo PDF: {str(e)}")
        
        self.ruta_archivo = ruta_archivo
        self.total_paginas = len(self.reader.pages)

    def extraer_texto_simple(self) -> str:
        texto_completo = ""
        for i, page in enumerate(self.reader.pages, start=1):
            try:
                contenido_pagina = page.extract_text()
                if not isinstance(contenido_pagina, str):
                    raise ValueError(f"El contenido extraído de la página {i} no es una cadena.")
                texto_completo += contenido_pagina
            except Exception as e:
                raise ValueError(f"Error al extraer texto de la página {i}: {str(e)}")
        return texto_completo
