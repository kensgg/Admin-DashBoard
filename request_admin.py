import requests

API_BASE_URL = "https://vercel-test-hcnx0zgf9-r3mat3rs-projects.vercel.app/api"

def agregar_administrador(username, email, password):
    """Registra un administrador."""
    url = f"{API_BASE_URL}/registroAdmin"
    data = {
        "username": username,
        "email": email,
        "password": password,
    }
    try:
        response = requests.post(url, json=data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error al agregar administrador: {e}")
        return False

def obtener_administradores():
    """Obtiene la lista de administradores."""
    try:
        response = requests.get(f"{API_BASE_URL}/showAdmins")
        if response.status_code == 200:
            return response.json().get("datos", [])
        return []
    except Exception as e:
        print(f"Error al obtener administradores: {e}")
        return []

def obtener_administrador_por_id(admin_id):
    """Obtiene un administrador por su ID."""
    try:
        response = requests.get(f"{API_BASE_URL}/showIdAdmin/{admin_id}")
        if response.status_code == 200:
            return response.json().get("datos", None)
        return None
    except Exception as e:
        print(f"Error al obtener administrador: {e}")
        return None

def eliminar_administrador(admin_id):
    """Elimina un administrador por su ID."""
    try:
        response = requests.delete(f"{API_BASE_URL}/deleteIdAdmin/{admin_id}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error al eliminar administrador: {e}")
        return False

def actualizar_administrador(admin_data):
    """Actualiza un administrador."""
    try:
        response = requests.patch(f"{API_BASE_URL}/updateIdAdmin", json=admin_data)
        print("Código de respuesta:", response.status_code)  # 🔎 Verifica el código de respuesta
        print("Respuesta del servidor:", response.text)  # 🔎 Imprime la respuesta completa del servidor
        return response.status_code == 200
    except Exception as e:
        print(f"Error al actualizar administrador: {e}")
        return False
