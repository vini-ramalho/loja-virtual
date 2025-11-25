# loja-virtual

> Projeto de estudo de arquitetura DDD + TDD — sistema básico de loja/pedidos em Python

## 🚀 Visão Geral

Este projeto foi criado com o objetivo de praticar e aplicar os conceitos de **Domain-Driven Design (DDD)** e **Test-Driven Development (TDD)** em Python. A ideia é simular um backend de “loja virtual” com domínio de pedidos, clientes, items, repositórios e serviços — tudo modelado seguindo boas práticas de separação de camadas e testes automatizados.

Principais objetivos:
- Modelar entidades de domínio (Order, Customer, OrderItem, OrderStatus) com lógica de negócio clara.  
- Separar camadas (domain, services, repositories) conforme padrão DDD.  
- Garantir qualidade e confiabilidade com testes automatizados (TDD).  

## 📂 Estrutura do projeto
```
LOJA-VIRTUAL/
├── src/ — código fonte
├── tests/ — testes automatizados (unitários / de serviço)
├── requirements.txt — dependências do projeto
├── main.py — ponto de entrada / exemplo de execução
└── ... — outros arquivos auxiliares (configurações, etc.)
```

### Destaques da arquitetura

- Camada de **domínio** com modelos como `Order`, `Customer`, `OrderItem`, `OrderStatus`.  
- Camada de **serviço** que orquestra lógica de uso (criação de pedido, validações, regras de negócio).  
- Repositórios — mocks ou implementações — para persistência.  
- Testes que validam comportamento antes da implementação (TDD).  

## 📚 Referências / Inspirações
- [Programador Python](https://www.youtube.com/@programadorpython)
- Toda base desse projeto foi retirada do canal do Programador Python, onde tomei a iniciativa de finalizar o projeto de acordo com minhas preferências

## Autor

Vinicius Ramalho – [LinkedIn](https://www.linkedin.com/in/vin%C3%ADcius-ramalho-3681a418b)
