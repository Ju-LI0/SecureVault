from app.models.credencial import Credencial
from app.services.gerador_senhas import GeradorDeSenhas


class Menu:

    @staticmethod
    def exibir():
        print("\n" + "=" * 35)
        print("          SECUREVAULT")
        print("=" * 35)
        print("1. Adicionar credencial")
        print("2. Listar credenciais")
        print("3. Buscar credencial")
        print("4. Remover credencial")
        print("5. Gerar senha")
        print("0. Sair")
        print("=" * 35)

    @staticmethod
    def solicitar_credencial():
        print("\n=== NOVA CREDENCIAL ===")

        servico = input("Serviço: ").strip()
        usuario = input("Usuário: ").strip()
        url = input("URL opcional: ").strip()

        print("\n1. Digitar senha")
        print("2. Gerar senha automaticamente")

        opcao_senha = input("Escolha uma opção: ").strip()

        if opcao_senha == "2":
            senha = GeradorDeSenhas.gerar()
            print("Senha gerada com sucesso!")
            print("Senha:", senha)
        else:
            senha = input("Senha: ")

        return Credencial(
            servico=servico,
            usuario=usuario,
            senha=senha,
            url=url or None
        )