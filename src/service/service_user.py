from src.models import user
from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.search_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuário adicionado"
            else:
                return "Parametros inválidos"

        else:
            return "Parametros inválidos"

    def search_user (self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def remove_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                self.store.bd.remove(user)
                return "Usuario removido"
        return "usuario nao encontrado"

    def update_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                for user in self.store.bd:
                    if user.name == name:
                        user.job = job
                        return "Usuário atualizado"
                return "Usuário não encontrado"
            else:
                return "Parâmetros inválidos"
        else:
            return "Parâmetros inválidos"


    def get_user_by_name(self, name):
        if isinstance(name, str) or name is None:
            for user in self.store.bd:
                if user.name == name:
                    return user
            return "Usuário não encontrado"
        else:
                return "Parâmetros inválidos"