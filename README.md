### API DE CONTROLE DE REVENDEDORES

## INSTALACAO
Em seu proprio env

```cmd
pipenv install
```

via docker
```cmd
docker-compose build
```


## RODANDO O PROJETO
via docker
```cmd
docker-compose up -d
```

em seu env
```cmd
pipenv run python api/app.py
```

## CRIANDO TABELAS
Primeiro criar um db chamado boticario

docker:
```cmd
 docker-compose exec db mysql -uroot -pexample -e 'create database boticario'
```

em seguida rodar alembic
```cmd
docker-compose exec web bash
pipenv run alembic upgrade heads
```
