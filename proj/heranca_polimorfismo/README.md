# Exercícios de Fixação: Herança e Polimorfismo em Python

Pratique os conceitos de reutilização de código através de classes filhas e modificação de comportamentos com polimorfismo.

---

### 1. A Classe Mãe 'Veiculo' (Super Fácil)
**Enunciado:**
Crie uma classe chamada `Veiculo` com o construtor `__init__` que recebe `marca` e `ano`. Depois, crie uma classe filha chamada `Carro` que herda de `Veiculo` mas não adiciona nenhum atributo ou método novo. Instancie um objeto de `Carro` e mostre sua marca.

---

### 2. Herdando Atributos de Família (Super Fácil)
**Enunciado:**
Crie uma classe `Pai` com um atributo de classe `cor_dos_olhos = 'Castanho'`. Crie uma classe `Filho` que herda de `Pai`. Sem criar nenhum código dentro da classe `Filho` (use apenas `pass`), instancie um objeto da classe `Filho` e printe a sua cor dos olhos.

---

### 3. Polimorfismo de Sons Animais (Super Fácil)
**Enunciado:**
Crie uma classe mãe `Animal` com um método `emitir_som(self)`. Esse método deve retornar a string `'Som genérico'`. Crie uma classe filha `Gato` que herda de `Animal` e sobrescreve o método `emitir_som(self)` para retornar `'Miau!'`.

---

### 4. Ativando o Construtor do Pai com super() (Fácil)
**Enunciado:**
Crie uma classe `Dispositivo` que recebe `nome` no construtor. Crie uma classe filha `Celular` que herda de `Dispositivo`. O construtor do `Celular` deve receber `nome` e `bateria` (inteiro), e usar obrigatoriamente `super().__init__(nome)` para salvar o nome na classe mãe.

---

### 5. Polimorfismo de Impressão de Documentos (Fácil)
**Enunciado:**
Crie uma classe mãe `Documento` com um método `exibir(self)` que retorna `'Texto genérico'`. Crie as classes filhas `PDF` (que retorna `'Exibindo arquivo PDF'`) e `Imagem` (que retorna `'Mostrando figura gráfica'`). Chame o método `exibir` de ambas em um laço de repetição.

---

### 6. Especialização de Conta Bancária (Fácil)
**Enunciado:**
Crie uma classe `Conta` com o atributo `saldo = 100`. Crie uma classe filha `ContaEstudante` que herda de `Conta` e adiciona o método `render_bonus(self)`, que adiciona de forma fixa 10 reais ao saldo atual.

---

### 7. Sons Diferentes na Mesma Lista (Médio)
**Enunciado:**
Crie uma classe mãe `Instrumento` com o método `tocar(self)`. Crie três subclasses: `Violao` (retorna `'Acorde de violão'`), `Flauta` (retorna `'Melodia doce'`) e `Bateria` (retorna `'Batida forte'`). Crie uma lista misturando esses instrumentos e use um laço `for` para fazer todos tocarem de forma polimórfica.

---

### 8. Polimorfismo com Parâmetros de Cálculo (Médio)
**Enunciado:**
Crie uma classe mãe `CalculadorDeImposto`. Ela tem um método `calcular(self, valor)` que retorna `valor * 0.05`. Crie uma classe filha `ImpostoArtigoLuxo` que sobrescreve esse método e calcula `valor * 0.20`. Teste o mesmo valor de entrada em instâncias das duas classes.

---

### 9. Estendendo o Comportamento do Pai (Médio)
**Enunciado:**
Crie uma classe `Funcionario` com um método `trabalhar(self)` que retorna `'Realizando tarefas básicas.'`. Crie a classe filha `Gerente`. O método `trabalhar(self)` do gerente deve usar `super().trabalhar()` para pegar o texto do funcionário e concatenar com o texto: `' e revisando relatórios da equipe.'`

---

### 10. O Ataque Polimórfico Customizado (Médio)
**Enunciado:**
Crie uma classe mãe `Heroi` com `nome` e `vida`. Crie a classe `Mago` (com atributo `poder_magico`) e `Guerreiro` (com `forca_fisica`). Ambas herdam de `Heroi`. Crie o método `atacar(self)` na classe mãe que avisa que não há arma. Sobrescreva o método `atacar(self)` no Mago para retornar o dano baseado no poder mágico + 10, e no Guerreiro baseado na força física * 2.

---

