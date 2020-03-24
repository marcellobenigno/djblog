# DjBlog
Um blog criado com Django.


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8.0
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure o .env
6. Crie um banco de dados PostgreSQL
7. Rode as migrações
8. Execute os testes.

```console
git clone git@github.com:marcellobenigno/djblog.git
cd djblog
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
createdb djblog
python manage.py migrate
python manage.py test
```


## Como instalar o tema do Django-Admin?

1. Carregue os dados a partir do arquivo `fixtures/admin_djblog.json`:


```console
python manage.py loaddata fixtures/admin_djblog.json
```
