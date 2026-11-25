# Pipeline CI/CD com Docker Hub

Fluxo: `lint` + `testes` (paralelo) -> build local -> scan Trivy -> push no Docker Hub.

## Configuracao (uma vez)
1. Docker Hub > Account Settings > Personal access tokens > crie um token com permissao Read & Write.
2. GitHub > repositorio > Settings > Secrets and variables > Actions > New repository secret:
   - `DOCKERHUB_USERNAME`: seu usuario do Docker Hub
   - `DOCKERHUB_TOKEN`: o token criado (nao use a senha da conta)
3. Copie esta estrutura para o repositorio e de push na `main`.

## Tags geradas
- `sha-abc1234` em todo push na main
- `latest` na main
- `1.2.3` ao criar a tag git `v1.2.3`

## Testar local
    pip install -r requirements-dev.txt && python -m pytest && flake8 app tests
    docker build -t cicd-demo . && docker run -p 8000:8000 cicd-demo
