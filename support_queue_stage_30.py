# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SupportQueue
import json
from pathlib import Path

PROFILE_DIR = Path(__file__).parent / "profiles"

def load_profiles():
    return json.loads((PROFILE_DIR / "profiles.json").read_text())

def save_profiles(profiles):
    (PROFILE_DIR / "profiles.json").write_text(json.dumps(profiles, indent=2))

def register_profile(name, role, priority=0):
    profiles = load_profiles()
    if name in profiles:
        raise ValueError(f"Profile '{name}' already exists")
    profiles[name] = {"role": role, "priority": priority}
    save_profiles(profiles)
    return profiles[name]

def get_profile(name):
    profiles = load_profiles()
    if name not in profiles:
        raise KeyError(f"Profile '{name}' not found")
    return profiles[name]

def list_profiles():
    return load_profiles()
