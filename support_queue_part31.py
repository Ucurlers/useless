# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SupportQueue
def switch_profile(self, profile_id):
        """Переключение активного профиля. Возвращает True если профиль найден."""
        profile = self.profiles.get(profile_id)
        if profile is None:
            return False
        self.active_profile_id = profile_id
        return True
