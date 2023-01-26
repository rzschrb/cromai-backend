
# Space Cromai Endpoint

Endpoint para a calculadora de teorema de pitagoras desenvolvido para o desafio do Space Cromai proposto pela Cromai.

Desenvolvido utilizando Python + Flask.

## Instalação

Clone o repositorio (estarei usando clone por HTTPS) e instale as dependencias utilizando o pip.

```bash
  git clone https://github.com/rzschrb/cromai-backend.git
  cd .\cromai-backend\
  pip install -r requirements.txt
```

Após as dependencias serem instaladas apenas utilize o comando do flask dentro da pasta com o arquivo `app.py` para iniciar o servidor.

```bash
  flask run
```

Ele irá abrir abrir um `localhost` na porta `5000` permitindo você acessar pelo seu navegador na seguinte url: `http://localhost:5000/`
    
## Documentação da API

#### Retorna resposta da rota principal

```http
  GET /
```

#### Retorna um calculo

```http
  GET /calculate/${cateto_a}/${cateto_b}/${hipotenusa}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `cateto_a`      | `string` | Valor do cateto A |
| `cateto_b`      | `string` | Valor do cateto B |
| `hipotenusa`      | `string` | Valor da hipotenusa|


## Uso/Exemplos

#### Como utilizar

Para calcular um dos lados apenas deixe o lado que deseja calcular como 0.

```http
  GET /calculate/21/20/0
```

Isso irá retornar um json, com o ID da mensagem e uma mensagem confirmando que é um triangulo retangulo e o valor final.

```json
{"id":"200","response":"É um triangulo retangulo com a hipotenusa C de: 29.00"}
```

