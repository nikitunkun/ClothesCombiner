# Clothes Combiner

## Description

One day my girlfriend told me that she had nothing to wear...
The project is a virtual closet in which you can load your clothes and see all possible combinations.

## Technologies

- [![Python](https://img.shields.io/static/v1?label=&message=Python&color=blue&logo=python&logoColor=white)](https://www.python.org/)
- [![Django](https://img.shields.io/static/v1?label=&message=Django&color=green&logo=django&logoColor=white)](https://www.djangoproject.com/)
- [![PostgreSQL](https://img.shields.io/static/v1?label=&message=PostgreSQL&color=blue&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## Install and Usage

### Install

- Clone or download the project
```bash
git clone 
```
- Navigate to the project directory
```bash
cd ClothesCombiner
```

### Configurate

- Configurate the ***.env.dist*** file

| Environment variable | Value                                      |
|:--------------------:|--------------------------------------------|
| SECRET_KEY           | Django Secret Key                          |
| DEBUG                | Debug (True for debugging or False)        |
| POSTGRES_HOST        | PostgreSQL Host                            |
| POSTGRES_PORT        | PostgreSQL Port                            |
| POSTGRES_USER        | PostgreSQL Username                        |
| POSTGRES_PASSWORD    | PostgreSQL Password                        |
| POSTGRES_DB_NAME     | PostgreSQL Database Name                   |

- Copy ***.env.dist*** to ***.env***
```
cp .env.dist .env
```

### Running

- To build project
```bash
docker-compose build
```

- To run project
```bash
docker-compose up
```

- Or Build and Run project
```bash
docker-compose up --build
```

- To load sample dump
```bash
docker-compose run combiner make load_data
```

- To create Super User (for admin panel)
```bash
docker-compose run combiner make admin
```

### Usage

- Open your browser and try it on
```
http://0.0.0.0:8000
```
- To open the Admin panel
```
http://0.0.0.0:8000/admin
```

## Enjoy 🙃