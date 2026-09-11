from app.models.credencial import Credencial
from app.repositories.cofre_repository import CofreRepository


class CofreService:
    def __init__(self, repository):
        if not isinstance(repository, CofreRepository):
            raise TypeError(
                "É necessário fornecer um CofreRepository."
            )

        self._repository = repository

    def adicionar(self, credencial):
        if not isinstance(credencial, Credencial):
            raise TypeError(
                "O objeto deve ser uma instância de Credencial."
            )

        if self._repository.existe(
            credencial.servico,
            credencial.usuario
        ):
            raise ValueError(
                "Já existe uma credencial cadastrada "
                "para esse serviço e usuário."
            )

        self._repository.salvar(credencial)

    def listar(self):
        return self._repository.listar()

    def buscar_por_servico(self, servico):
        return self._repository.buscar_por_servico(servico)

    def remover_por_servico(self, servico):
        return self._repository.remover_por_servico(servico)

    @property
    def quantidade(self):
        return len(self.listar())