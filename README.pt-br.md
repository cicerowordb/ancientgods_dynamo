# Deuses Antigos

O Banco de Dados dos Deuses Antigos é um projeto destinado a catalogar e apresentar informações detalhadas sobre figuras mitológicas de civilizações antigas. Este aplicativo explora o mundo da mitologia, tornando-o acessível para usuários que desejam descobrir as histórias, atributos e significados culturais dos deuses antigos.

Desenvolvido como parte do curso de DevOps pela Academia DevOps, este projeto tem um propósito didático. Ele demonstra a aplicação prática dos princípios de DevOps, incluindo integração contínua, implantação e infraestrutura como código. O objetivo é proporcionar a estudantes e entusiastas uma experiência prática no desenvolvimento, implantação e gerenciamento de um aplicativo do mundo real em um ambiente DevOps.

O aplicativo está aberto a modificações ou extensões, refletindo o espírito colaborativo e adaptável da cultura DevOps. Seja para adicionar novos recursos, melhorar funcionalidades ou adaptá-lo a uma mitologia diferente, você é incentivado a explorar e inovar.

Os dados para este projeto, incluindo a lista de deuses e seus atributos, são provenientes do projeto open-source disponível em [kamiranoff/greek-mythology-data](https://github.com/kamiranoff/greek-mythology-data/blob/master/package.json). Agradecemos aos contribuidores deste projeto por fornecerem um recurso inestimável que torna este aplicativo possível. Se alguma informação neste arquivo JSON estiver incorreta, entre em contato diretamente com o responsável, pois não avaliamos o conteúdo dos dados.

## Como executar localmente

Este é um aplicativo em Python 3. Ele utiliza Flask e Jinja2 para o frontend, e Flask com DynamoDB para o backend. Um container Docker é usado para executar o DynamoDB localmente.

### Pré-requisitos

Para executar este aplicativo localmente, você precisará de:
- Docker
- Python 3
- Python 3-pip
- Python 3-venv
- Pylint (opcional, para verificações de estilo de código)

O comando `make` fornece as seguintes opções para gerenciar o aplicativo:

```bash
make
```

<code>use one option: run-frontend-local, run-backend-local, run-all-local, pylint-backend, pylint-frontend, run-frontend-local-quiet, run-backend-local-quiet, run-all-local-quiet</code>

Opções disponíveis:
- `run-frontend-local`: Executa o frontend localmente.
- `run-backend-local`: Executa o backend localmente.
- `run-all-local`: Executa o frontend e o backend localmente.
- `pylint-backend`: Verifica o estilo de código do backend.
- `pylint-frontend`: Verifica o estilo de código do frontend.
- `run-frontend-local-quiet`: Executa o frontend localmente com logs mínimos.
- `run-backend-local-quiet`: Executa o backend localmente com logs mínimos.
- `run-all-local-quiet`: Executa o frontend e o backend localmente com logs mínimos.

Para executar todo o aplicativo localmente com logs detalhados, use o seguinte comando. Note que ele utiliza as portas TCP 5000 e 5001:

```bash
make run-all-local
```

Para executar o aplicativo com logs mínimos, use:

```bash
make run-all-local-quiet
```

## Como verificar

Para verificar o estilo de código do backend:

```bash
make pylint-backend
```

A saída indicará a avaliação do código. Exemplo:

<code>--------------------------------------------------------------------<br>
Seu código foi avaliado em 10.00/10 (execução anterior: 10.00/10, +0.00)</code>

Para verificar o estilo de código do frontend:

```bash
make pylint-frontend
```

A saída indicará a avaliação do código. Exemplo:

<code>--------------------------------------------------------------------<br>
Seu código foi avaliado em 10.00/10 (execução anterior: 10.00/10, +0.00)</code>

## Problemas conhecidos e trabalhos futuros

- Ao tentar remover uma entidade inexistente, o código fornece um feedback positivo em vez de uma mensagem de erro. Apenas um problema de mensagem.
- É necessário um script para construir a imagem Docker para facilitar a implantação.
- Testes unitários ainda não foram implementados e são necessários.
- Testes de integração também são necessários para garantir a funcionalidade geral do sistema.
- Somente o backend está adaptado para português e inglês.
