
import secrets
import string


class GeradorDeSenhas:

    @staticmethod
    def gerar(
        tamanho=16,
        incluir_maiusculas=True,
        incluir_minusculas=True,
        incluir_numeros=True,
        incluir_simbolos=True
    ):
        if tamanho < 4:
            raise ValueError("O tamanho mínimo da senha é 4 caracteres.")

        caracteres = ""

        if incluir_maiusculas:
            caracteres += string.ascii_uppercase

        if incluir_minusculas:
            caracteres += string.ascii_lowercase

        if incluir_numeros:
            caracteres += string.digits

        if incluir_simbolos:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("É necessário selecionar pelo menos um tipo de caractere.")

        senha = "".join(
            secrets.choice(caracteres)
            for _ in range(tamanho)
        )

        return senha