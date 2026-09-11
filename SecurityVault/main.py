from getpass import getpass
from app.services.cofre_service import CofreService
from app.repositories.cofre_repository import CofreRepository
from app.security.criptografia import CriptografiaService
from app.services.gerador_senhas import GeradorDeSenhas
from app.ui.menu import Menu


def main():
    print("=== SECUREVAULT ===\n")

    senha_mestra = getpass(
        "Digite sua senha mestra: "
    )

    criptografia = CriptografiaService(
        senha_mestra
    )

    repository = CofreRepository(
        criptografia=criptografia
    )

    cofre = CofreService(
        repository=repository
    )

    while True:
        Menu.exibir()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                credencial = Menu.solicitar_credencial()

                cofre.adicionar(credencial)

                print("\nCredencial adicionada com sucesso!")

            except (ValueError, TypeError) as erro:
                print(f"\nErro: {erro}")

        elif opcao == "2":
            print("\n=== CREDENCIAIS SALVAS ===")

            credenciais = cofre.listar()

            if not credenciais:
                print("Nenhuma credencial cadastrada.")
            else:
                for indice, credencial in enumerate(
                    credenciais,
                    start=1
                ):
                    print(
                        f"{indice}. "
                        f"{credencial.exibir_resumo()}"
                    )

        elif opcao == "3":
            servico = input(
                "\nDigite o nome do serviço: "
            ).strip()

            credencial = cofre.buscar_por_servico(
                servico
            )
        elif opcao == "3":
            print("\n=== BUSCAR CREDENCIAL ===")

            servico = input(
                "Digite o nome do serviço: "
            ).strip()

            usuario = input(
                "Digite o usuário ou e-mail: "
            ).strip()

            credencial = cofre.buscar(
                servico,
                usuario
            )

            if credencial:
                print("\nCredencial encontrada:")
                print(credencial.exibir_resumo())
                
            else:
                print("\nCredencial não encontrada.")
            if credencial:
                print(
                    "\nCredencial encontrada:"
                )
                print(
                    credencial.exibir_resumo()
                )
            else:
                print(
                    "\nCredencial não encontrada."
                )

        elif opcao == "4":
            servico = input(
                "\nDigite o serviço que deseja remover: "
            ).strip()

            removida = cofre.remover_por_servico(
                servico
            )

            if removida:
                print(
                    "\nCredencial removida com sucesso!"
                )
            else:
                print(
                    "\nCredencial não encontrada."
                )

        elif opcao == "5":
            try:
                tamanho = int(
                    input(
                        "\nDigite o tamanho da senha: "
                    )
                )

                senha = GeradorDeSenhas.gerar(
                    tamanho=tamanho
                )

                print("\nSenha gerada:")
                print(senha)

            except ValueError as erro:
                print(f"\nErro: {erro}")

        elif opcao == "0":
            print("\nEncerrando o SecureVault...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()