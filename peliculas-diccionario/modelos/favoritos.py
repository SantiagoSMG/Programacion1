import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAV_PATH = os.path.join(BASE_DIR, "favoritos.json")

# Cargar favoritos
def _load():
    if not os.path.exists(FAV_PATH):
        return set()
    try:
        with open(FAV_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data)
    except Exception:
        return set()

# Guardar favoritos
def _save(s):
    try:
        with open(FAV_PATH, "w", encoding="utf-8") as f:
            json.dump(list(s), f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error guardando favoritos:", e)

# API pública
def get_all():
    return sorted(list(_load()))

def is_favorite(title):
    s = _load()
    return title in s

def add_favorite(title):
    s = _load()
    s.add(title)
    _save(s)

def remove_favorite(title):
    s = _load()
    if title in s:
        s.remove(title)
        _save(s)

def toggle_favorite(title):
    if is_favorite(title):
        remove_favorite(title)
        return False
    else:
        add_favorite(title)
        return True