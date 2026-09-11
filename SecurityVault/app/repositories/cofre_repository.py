import sqlite3
from pathlib import Path
from app.models.credencial import Credencial
from app.security.criptografia import CriptografiaService


class CofreRepository:
    def __init__(
        self,
        criptografia,
        caminho_banco="data/securevault.db"
    ):
        if not isinstance(criptografia, CriptografiaService):
            raise TypeError(
                "É necessário fornecer um CriptografiaService."
            )

        self._criptografia = criptografia
        self._caminho_banco = Path(caminho_banco)

        self._caminho_banco.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self._caminho_banco)

    def _criar_tabela(self):
        with self._conectar() as conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS credenciais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    servico TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    url TEXT,
                    UNIQUE(servico, usuario)
                )
            """)

    def salvar(self, credencial):
        if not isinstance(credencial, Credencial):
            raise TypeError(
                "O objeto deve ser uma instância de Credencial."
            )

        senha_criptografada = self._criptografia.criptografar(
            credencial._senha
        )

        with self._conectar() as conexao:
            conexao.execute("""
                INSERT INTO credenciais (
                    servico,
                    usuario,
                    senha,
                    url
                )
                VALUES (?, ?, ?, ?)
            """, (
                credencial.servico,
                credencial.usuario,
                senha_criptografada,
                credencial.url
            ))

    def listar(self):
        with self._conectar() as conexao:
            registros = conexao.execute("""
                SELECT servico, usuario, senha, url
                FROM credenciais
                ORDER BY servico
            """).fetchall()

        credenciais = []

        for registro in registros:
            senha_descriptografada = (
                self._criptografia.descriptografar(registro[2])
            )

            credencial = Credencial(
                servico=registro[0],
                usuario=registro[1],
                senha=senha_descriptografada,
                url=registro[3]
            )

            credenciais.append(credencial)

        return credenciais

    def buscar_por_servico(self, servico):
        with self._conectar() as conexao:
            registro = conexao.execute("""
                SELECT servico, usuario, senha, url
                FROM credenciais
                WHERE LOWER(servico) = LOWER(?)
                LIMIT 1
            """, (servico,)).fetchone()

        if registro is None:
            return None

        senha_descriptografada = (
            self._criptografia.descriptografar(registro[2])
        )

        return Credencial(
            servico=registro[0],
            usuario=registro[1],
            senha=senha_descriptografada,
            url=registro[3]
        )

    def remover_por_servico(self, servico):
        with self._conectar() as conexao:
            cursor = conexao.execute("""
                DELETE FROM credenciais
                WHERE LOWER(servico) = LOWER(?)
            """, (servico,))

            return cursor.rowcount > 0

    def existe(self, servico, usuario):
        with self._conectar() as conexao:
            registro = conexao.execute("""
                SELECT id
                FROM credenciais
                WHERE LOWER(servico) = LOWER(?)
                AND LOWER(usuario) = LOWER(?)
                LIMIT 1
            """, (
                servico,
                usuario
            )).fetchone()

        return registro is not None

    def buscar(self, servico, usuario):
        with self._conectar() as conexao:
            registro = conexao.execute("""
                SELECT servico, usuario, senha, url
                FROM credenciais
                WHERE LOWER(servico) = LOWER(?)
                AND LOWER(usuario) = LOWER(?)
                LIMIT 1
            """, (
                servico,
                usuario
            )).fetchone()

        if registro is None:
            return None

        senha_descriptografada = (
            self._criptografia.descriptografar(registro[2])
        )

        return Credencial(
            servico=registro[0],
            usuario=registro[1],
            senha=senha_descriptografada,
            url=registro[3]
        )