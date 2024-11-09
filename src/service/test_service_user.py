import unittest

from src.models.user import User
from src.service.service_user import ServiceUser


class TestServiceUser(unittest.TestCase):

    def setUp(self):
        self.service = ServiceUser()

    def test_add_user_successful(self):
        result = self.service.add_user("Antonio", "Analista")
        self.assertEqual(result, "Usuário adicionado")
        self.assertEqual(len(self.service.store.bd), 1)

    def test_remove_user_successful(self):
        self.service.add_user("Antonio", "Analista")
        result = self.service.remove_user("Antonio")
        self.assertEqual(result, "Usuario removido")
        self.assertEqual(len(self.service.store.bd), 0)

    def test_update_user_successful(self):
        self.service.add_user("Antonio", "Desenvolvedor")
        result = self.service.update_user("Antonio", "Analista")
        self.assertEqual(result, "Usuário atualizado")

    def test_get_user_by_name(self):
        self.service.add_user("Antonio", "Analista")
        user = self.service.get_user_by_name("Antonio")
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Antonio")
        self.assertEqual(user.job, "Analista")