# FastAPI + GraalPy Demo

Demonstração de uma API FastAPI/Python rodando sobre GraalVM Python (GraalPy), com suporte a execução em container (JIT ou AOT), focada em compatibilidade, performance e portabilidade sem dependências nativas C.

## Pré-requisitos

- [Podman](https://podman.io/) ou [Docker](https://www.docker.com/)
- Arquivos do projeto nesta pasta (incluindo `Containerfile` e `requirements.txt`)

## Como Buildar e Rodar (JIT)

### 1. Build da imagem

```sh
podman build -t fastapi-graalpy:jit -f Containerfile .
# ou
docker build -t fastapi-graalpy:jit -f Containerfile .
```

### 2. Rodar o container

```sh
podman run --rm -p 8000:8000 fastapi-graalpy:jit
# ou
docker run --rm -p 8000:8000 fastapi-graalpy:jit
```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

## Endpoints

- `GET /` — Hello World
- `GET /items/{item_id}` — Retorna item e query string
- `GET /heavy-counter?n=100000000` — Endpoint pesado para teste de performance

## Observações

- O container usa GraalPy (GraalVM Python) para rodar FastAPI sem dependências nativas C.
- O comando de entrada força o uso de `uvicorn` puro (`--http h11 --loop asyncio`).

---
