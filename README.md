# API de Gestão de Estoque

Este projeto é uma API para gestão de estoque desenvolvida com Flask, utilizando o padrão MVC. A API permite gerenciar produtos, categorias, fornecedores, lotes e movimentações de estoque.

## Estrutura do Projeto

```md
API-estoque/
├── app.py
├── config.py
├── database.py
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── batch.py
│   ├── category.py
│   ├── supplier.py
│   └── stock_movement.py
├── services/
│   ├── __init__.py
│   ├── product.py
│   ├── batch.py
│   ├── category.py
│   ├── supplier.py
│   └── stock_movement.py
├── controllers/
│   ├── __init__.py
│   ├── product.py
│   ├── batch.py
│   ├── category.py
│   ├── supplier.py
│   └── stock_movement.py
└── README.md
```


## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/API-estoque.git
    cd API-estoque
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure a URL do banco de dados no arquivo `config.py`:
    ```python
    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///estoque.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

5. Inicie a aplicação:
    ```sh
    python app.py
    ```

## Endpoints

### Produtos

- **GET /api/products**: Lista todos os produtos.
    ```sh
    curl -X GET http://127.0.0.1:5000/api/products
    ```

### Categorias

- **GET /api/categories**: Lista todas as categorias.
    ```sh
    curl -X GET http://127.0.0.1:5000/api/categories
    ```

### Fornecedores

- **GET /api/suppliers**: Lista todos os fornecedores.
    ```sh
    curl -X GET http://127.0.0.1:5000/api/suppliers
    ```

### Lotes

- **GET /api/batches**: Lista todos os lotes.
    ```sh
    curl -X GET http://127.0.0.1:5000/api/batches
    ```

### Movimentações de Estoque

- **GET /api/stock_movements**: Lista todas as movimentações de estoque.
    ```sh
    curl -X GET http://127.0.0.1:5000/api/stock_movements
    ```

## Estrutura dos Modelos

### Produto (Product)

- `id`: ID do produto (PK)
- `name`: Nome do produto
- `description`: Descrição do produto
- `price`: Preço do produto
- `supplier_id`: ID do fornecedor (FK)
- `categories`: Relacionamento muitos-para-muitos com categorias

### Categoria (Category)

- `id`: ID da categoria (PK)
- `name`: Nome da categoria

### Fornecedor (Supplier)

- `id`: ID do fornecedor (PK)
- `name`: Nome do fornecedor
- `contact_id`: ID do contato (FK)

### Lote (Batch)

- `id`: ID do lote (PK)
- `product_id`: ID do produto (FK)
- `batch_code`: Código do lote
- `arrival_date`: Data de chegada
- `expiry_date`: Data de validade
- `quantity`: Quantidade

### Movimentação de Estoque (StockMovement)

- `id`: ID da movimentação (PK)
- `batch_id`: ID do lote (FK)
- `movement_type`: Tipo de movimentação (entrada/saída)
- `quantity`: Quantidade
- `movement_date`: Data da movimentação
