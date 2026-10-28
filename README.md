# TDE 3: BDD (Tradicional) vs. TDD

## 1. Repositório do Projeto
* **GitHub:** [edu292/tradicional-vs-tdd](https://github.com/edu292/tradicional-vs-tdd)

## 1. Registro da Etapa 1
* **Tempo gasto para escrever os testes:** ~20 minutos.
* **Dificuldades e observações:** Escrever os testes com a implementação já pronta traz uma tendência pensar nos casos em função da lógica e fluxos do código ao invés do problema em si. Nesse caso a suíte de testes foi capaz encontrar um bug na implementação original, onde um dos fluxos retornava o próprio valor de entrada (`valor_items`) sem aplicar as modificações devidas.

---

## 3. Momento da Verificação e da Validação

| Atividade | Abordagem Tradicional (Code First) | Abordagem TDD (Test First) |
| :--- | :--- | :--- |
| **Verificação** | Ocorreu **após** a implementação completa, quando os testes unitários foram executados e apontaram o erro do retorno de valor incorreto. | Ocorreu de forma **contínua** a cada ciclo, garantindo que cada linha de código criada já nascesse verificada. |
| **Validação** | Ocorreu de forma mental e informal **durante** a leitura inicial do enunciado para codificar tudo de uma vez, sendo confirmada apenas no fim. | Ocorreu **antes** de cada implementação, ao traduzir a expectativa de negócio do cliente diretamente em cenários de teste executáveis. |

---

## 4. Impacto da Inversão na Verificação Estática e Dinâmica

### Verificação Estática (Análise de Requisitos e Design)
* **Tradicional:** A análise de requisitos e o design da função foram feitos de cabeça antes do código. Isso facilitou pequenos descuidos de lógica.
* **TDD:** Escrever o teste primeiro força a verificação estática a acontecer **na criação do teste**. Para escrever o `assert`, foi necessário analisar com precisão as entradas, saídas, limites (ex: R$ 500,00 vs R$ 500,01) e até evoluir a assinatura da função antes mesmo de pensar no `if/else`. O teste atua como uma especificação formal e ferramenta de design.

### Verificação Dinâmica (Execução dos Testes)
* **Tradicional:** Funcionou como uma **auditoria tardia (caça a bugs)**. Os testes rodaram sobre um sistema fechado para descobrir o que já estava quebrado, exigindo retrabalho para corrigir o retorno do valor de entrada.
* **TDD:** Funcionou como um **guia de progresso e rede de segurança**. A execução confirmava que o requisito atual foi atendido e impedia que regras novas quebrassem as anteriores.
