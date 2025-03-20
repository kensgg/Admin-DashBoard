from tkinter import E
import requests

API_BASE_URL = "https://vercel-test-hcnx0zgf9-r3mat3rs-projects.vercel.app/api"


#usuarios
def obtener_usuarios():
    try:
        response = requests.get(f"{API_BASE_URL}/show")
        if response.status_code == 200:
            resultado = response.json()  # Convertir respuesta a JSON
            return resultado.get("datos", [])  # Extraer solo la lista de usuarios
        else:
            print(f"Error al obtener usuarios: {response.status_code} - {response.text}")
            return [] 
    except Exception as e:
        print(f"Excepción al obtener usuarios: {e}")
        return []  

def obtener_usuario_por_id(id_usuario):
    try:
        url = f"{API_BASE_URL}/showId/{id_usuario}"
        print(f"Solicitando usuario en: {url}")  # Verifica la URL generada

        response = requests.get(url)

        print(f"Respuesta de la API: {response.status_code} - {response.text}")  # Imprime la respuesta completa

        if response.status_code == 200:
            resultado = response.json()
            return resultado.get("datos", {})  # ✅ Corrección aquí
        else:
            print(f"Error al obtener usuario por ID: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Excepción al obtener usuario por ID: {e}")
        return None


def agregar_usuario(usuario):
    response = requests.post(f"{API_BASE_URL}/registro", json=usuario)
    return response.status_code == 200


def actualizar_usuario(usuario):
    # URL de la API para actualizar el usuario
    url = "https://vercel-test-hcnx0zgf9-r3mat3rs-projects.vercel.app/api/updateId"
    
    # Crear el cuerpo de la solicitud con los datos del usuario
    data = {
        "_id": usuario["id"],  # Asegúrate de incluir el id del usuario
        "sonName": usuario["sonName"],  # Nuevo valor para sonName
        "email": usuario["email"],  # Nuevo valor para email
        "password": usuario["password"]  # Nuevo valor para password, si se ha cambiado
    }

    try:
        # Realizar la solicitud PATCH a la API
        response = requests.patch(url, json=data)

        # Verificar si la respuesta fue exitosa (status code 200)
        if response.status_code == 200:
            print(f"Usuario actualizado correctamente: {response.json()['mensaje']}")
            return True
        else:
            print(f"❌ Error al actualizar el usuario: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error al hacer la solicitud: {e}")
        return False




def eliminar_usuario(id_usuario):
    response = requests.delete(f"{API_BASE_URL}/deleteId/{id_usuario}")
    return response.status_code == 200


