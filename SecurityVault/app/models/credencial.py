# Versão inicial da classe Credencial
# Esta classe representa uma credencial de acesso a um serviço
# contendo informações como serviço, usuário, senha e URL opcional.

class Credencial:
    def __init__(self, servico, usuario, senha, url=None):
        self._validar_dados(servico, usuario, senha)

        self._servico = servico
        self._usuario = usuario
        self._senha = senha
        self._url = url

    @staticmethod
    def _validar_dados(servico, usuario, senha):
        if not servico or not servico.strip():
            raise ValueError("O serviço não pode estar vazio.")

        if not usuario or not usuario.strip():
            raise ValueError("O usuário não pode estar vazio.")

        if not senha or not senha.strip():
            raise ValueError("A senha não pode estar vazia.")

    @property
    def servico(self):
        return self._servico

    @property
    def usuario(self):
        return self._usuario

    @property
    def url(self):
        return self._url

    def exibir_resumo(self):
        return f"{self.servico} | {self.usuario}"