import base64
import os
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class CriptografiaService:
    def __init__(
        self,
        senha_mestra,
        caminho_salt="data/salt.bin"
    ):
        if not senha_mestra or not senha_mestra.strip():
            raise ValueError(
                "A senha mestra não pode estar vazia."
            )

        self._caminho_salt = Path(caminho_salt)

        self._caminho_salt.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._salt = self._carregar_ou_criar_salt()

        self._chave = self._derivar_chave(
            senha_mestra
        )

        self._fernet = Fernet(self._chave)

    def _carregar_ou_criar_salt(self):
        if self._caminho_salt.exists():
            return self._caminho_salt.read_bytes()

        salt = os.urandom(16)

        self._caminho_salt.write_bytes(salt)

        return salt

    def _derivar_chave(self, senha_mestra):
        kdf = Scrypt(
            salt=self._salt,
            length=32,
            n=2**14,
            r=8,
            p=1
        )

        chave = kdf.derive(
            senha_mestra.encode("utf-8")
        )

        return base64.urlsafe_b64encode(chave)

    def criptografar(self, texto):
        if not isinstance(texto, str):
            raise TypeError(
                "O texto deve ser uma string."
            )

        return self._fernet.encrypt(
            texto.encode("utf-8")
        ).decode("utf-8")

    def descriptografar(self, texto_criptografado):
        if not isinstance(texto_criptografado, str):
            raise TypeError(
                "O texto criptografado deve ser uma string."
            )

        try:
            return self._fernet.decrypt(
                texto_criptografado.encode("utf-8")
            ).decode("utf-8")

        except InvalidToken:
            raise ValueError(
                "Não foi possível descriptografar. "
                "A senha mestra pode estar incorreta "
                "ou os dados foram alterados."
            )