import os
import requests
from typing import List, Tuple

class EnviadorOpenAI:
    def __init__(self, modelo: str, api_key: str = None):
        self.modelo = modelo
        self.url = "https://api.openai.com/v1/chat/completions"
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("La clave API de OpenAI no está configurada.")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _enviar_solicitud(self, mensajes: List[dict], max_tokens: int) -> Tuple[str, int, int, int]:
        try:
            data = {
                "model": self.modelo,
                "messages": mensajes,
                "max_tokens": max_tokens
            }

            response = requests.post(self.url, headers=self.headers, json=data)
            response.raise_for_status()
            response_json = response.json()
            contenido = response_json['choices'][0]['message']['content']
            tokens_enviados = response_json['usage']['prompt_tokens']
            tokens_recibidos = response_json['usage']['completion_tokens']
            tokens_totales = response_json['usage']['total_tokens']
            return contenido, tokens_enviados, tokens_recibidos, tokens_totales 
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud a OpenAI: {str(e)}")
            return "", 0, 0, 0

    def enviar_texto(self, contenido: str, prompt: List[dict], max_tokens: int = 5000) -> Tuple[str, int, int, int]:
        mensajes = [
            {"role": "system", "content": prompt[0]["content"]},
            {"role": "user", "content": prompt[1]["content"].format(texto=contenido)}
        ]
        
        return self._enviar_solicitud(mensajes, max_tokens)

