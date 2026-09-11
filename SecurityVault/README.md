# 🔐 SecureVault

O **SecureVault** é um gerenciador local de credenciais desenvolvido em Python.

O projeto permite cadastrar, listar, buscar e remover credenciais, além de gerar senhas seguras e armazenar as senhas de forma criptografada em um banco de dados SQLite.

Este projeto foi desenvolvido com foco em aprendizado de **Python, Programação Orientada a Objetos, organização de código, banco de dados e conceitos de CyberSecurity**.

---

## 📸 Sobre o projeto

O SecureVault funciona através de uma interface de terminal e possui uma estrutura organizada em camadas, separando:

- Modelos;
- Serviços;
- Segurança;
- Repositórios;
- Interface de usuário.

As senhas armazenadas no banco de dados não são salvas em texto puro. Antes de serem armazenadas, elas são criptografadas utilizando uma chave derivada da senha mestra do usuário.

---

## ✨ Funcionalidades

- [x] Cadastro de credenciais;
- [x] Geração automática de senhas;
- [x] Listagem de serviços cadastrados;
- [x] Busca de credenciais;
- [x] Remoção de credenciais;
- [x] Bloqueio de credenciais duplicadas;
- [x] Criptografia de senhas;
- [x] Derivação de chave utilizando Scrypt;
- [x] Armazenamento local com SQLite;
- [x] Validação de dados;
- [x] Tratamento de erros;
- [x] Uso de senha mestra;
- [x] Organização utilizando Programação Orientada a Objetos.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.13+**
- **SQLite**
- **Cryptography**
- **Scrypt**
- **Fernet**
- **Git e GitHub**

---

## 📂 Estrutura do projeto

```text
SecureVault/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── app/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── credencial.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gerador_senhas.py
│   │   └── cofre_service.py
│   │
│   ├── security/
│   │   ├── __init__.py
│   │   └── criptografia.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── cofre_repository.py
│   │
│   └── ui/
│       ├── __init__.py
│       └── menu.py
│
├── data/
│   └── .gitkeep
│
└── tests/
```

> Os arquivos reais do banco de dados e do salt não devem ser enviados ao GitHub.

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, você precisa ter instalado:

- Python 3.13 ou superior;
- Git, caso queira versionar o projeto;
- Um terminal, como PowerShell, CMD ou terminal do VS Code.

Você pode verificar a versão do Python com:

```bash
python --version
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

### 2. Acesse a pasta do projeto

```bash
cd SecureVault
```

### 3. Crie um ambiente virtual

No Windows:

```powershell
python -m venv venv
```

### 4. Ative o ambiente virtual

No PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No CMD:

```cmd
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o projeto

```bash
python main.py
```

---

## 🖥️ Exemplo de uso

Ao iniciar o sistema, será solicitada a senha mestra:

```text
=== SECUREVAULT ===

Digite sua senha mestra:
```

Depois, o menu principal será exibido:

```text
===================================
          SECUREVAULT
===================================
1. Adicionar credencial
2. Listar credenciais
3. Buscar credencial
4. Remover credencial
5. Gerar senha
0. Sair
===================================
```

---

## 🔒 Segurança

O SecureVault utiliza alguns recursos para proteger as credenciais:

### Senha mestra

A senha mestra é utilizada para derivar a chave de criptografia. Ela não deve ser armazenada diretamente no código ou no banco de dados.

### Scrypt

O projeto utiliza o algoritmo **Scrypt** para derivar uma chave criptográfica a partir da senha mestra.

O Scrypt foi desenvolvido para dificultar ataques de força bruta e ataques utilizando hardware especializado.

### Salt

Um salt aleatório é criado e armazenado no arquivo:

```text
data/salt.bin
```

Esse arquivo é necessário para que a mesma senha mestra gere a mesma chave posteriormente.

### Fernet

As senhas são criptografadas utilizando o **Fernet**, que fornece criptografia simétrica autenticada.

---

## ⚠️ Avisos importantes

Este projeto possui finalidade educacional e não deve ser considerado um gerenciador de senhas pronto para produção.

Recomendações:

- Não compartilhe sua senha mestra;
- Não envie o arquivo `data/securevault.db` para o GitHub;
- Não envie o arquivo `data/salt.bin` para o GitHub;
- Faça backups seguros;
- Não utilize senhas reais importantes durante os testes;
- Nunca coloque chaves ou senhas diretamente no código;
- Caso perca a senha mestra, os dados criptografados poderão não ser recuperados.

---

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto, foram praticados:

- Variáveis e funções em Python;
- Classes e objetos;
- Encapsulamento;
- Propriedades com `@property`;
- Métodos estáticos;
- Validação de dados;
- Tratamento de exceções;
- Separação de responsabilidades;
- Arquitetura em camadas;
- Banco de dados SQLite;
- Criptografia simétrica;
- Derivação de chaves;
- Geração segura de senhas;
- Manipulação de arquivos;
- Ambientes virtuais;
- Git e GitHub.

---

## 🔮 Melhorias futuras

Possíveis melhorias para versões futuras:

- [ ] Editar credenciais existentes;
- [ ] Interface gráfica;
- [ ] Interface web;
- [ ] Autenticação com múltiplos usuários;
- [ ] Copiar senhas para a área de transferência;
- [ ] Ocultar senhas geradas no terminal;
- [ ] Sistema de categorias;
- [ ] Exportação e importação segura;
- [ ] Backup criptografado;
- [ ] Testes automatizados;
- [ ] Auditoria de segurança das senhas;
- [ ] Verificador de força das senhas;
- [ ] Timeout automático por inatividade.

---

## 👨‍💻 Autor

Desenvolvido por **Fomenta Vale**.

Projeto criado para fins de estudo e aprimoramento em Python, Programação Orientada a Objetos e CyberSecurity.

---

## 📄 Licença

Este projeto está disponível para fins educacionais.
