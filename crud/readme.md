## Como acessar a API

1. **Clone** este repositório para o seu ambiente local:
    ```
    git clone https://github.com/pedro18x/treinamentoFabrica
    ```
2. Abra a pasta crud dentro do diretório na sua IDE

3. Certifique-se de ter o **Python 3.x** instalado em seu sistema.

4. Instale as dependências necessárias. Dentro do diretório do projeto, execute o seguinte comando:
    ```
    pip install -r requirements.txt
    ```

5. Execute as **migrações** do Django para criar o banco de dados:
    ```
    python manage.py migrate
    ```

6. Inicie o **servidor de desenvolvimento**:
    ```
    python manage.py runserver
    ```

7. Agora você pode acessar a API por meio do seguinte URL:
    ```
    http://localhost:8000/api/
    ```
