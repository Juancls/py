# Relatorio tecnico do ultimo commit

## Identificacao do commit
- Hash: `4b4770b3c4da10136545893b25450b29f9c31a1a`
- Autor: Victor-Lis <victorlisbronzo1@gmail.com>
- Data: 2026-04-07 18:46:02 -0300
- Mensagem: `fix: remove duplicate logs for student grades`
- Branch no momento da leitura: `master` (HEAD)

## Resumo estatistico
- Arquivos alterados: 1
- Insercoes: 4
- Remocoes: 7
- Arquivo impactado: `exDicionario.py`

## Mudancas tecnicas detalhadas

### 1) Ajuste de formatacao de prompt no cadastro
Trecho alterado na entrada de nome do aluno:
- Antes: `input("Nome aluno: ")`
- Depois: `input("\nNome aluno: ")`

**Efeito tecnico**
- Inclui quebra de linha antes do prompt de cadastro.
- Melhora separacao visual entre iteracoes do loop.
- Nao altera regra de negocio nem estrutura de dados.

### 2) Remocao de linhas em branco excedentes
Foram removidas linhas vazias entre o fim do primeiro `while` e o inicio do segundo `while`.

**Efeito tecnico**
- Reduz ruido visual no codigo.
- Sem impacto funcional.

### 3) Ajuste de formatacao de prompt na consulta
Trecho alterado ao iniciar a escolha do aluno:
- Antes: `print("Deseja ver a nota de qual aluno: ")`
- Depois: `print("\nDeseja ver a nota de qual aluno: ")`

**Efeito tecnico**
- Inclui quebra de linha antes do bloco de consulta.
- Melhora legibilidade da saida no terminal.
- Sem impacto na logica de consulta.

### 4) Correcao do escopo de impressao da media (fix principal)
Bloco alterado dentro da verificacao `if escolha in notas:`:
- Antes, as linhas de media estavam dentro do `for i in range(2)`.
- Depois, as linhas de media foram movidas para fora do `for`.

Representacao logica:
- Antes:
  - Para cada nota (2 iteracoes), imprimia a nota e em seguida imprimia a media.
  - Resultado: media repetida 2 vezes.
- Depois:
  - Imprime as 2 notas no loop.
  - Imprime a media uma unica vez apos finalizar o loop.

**Efeito tecnico**
- Elimina log duplicado de media para o mesmo aluno.
- Mantem o mesmo calculo: `(nota1 + nota2) / 2`.
- Altera somente o fluxo de exibicao (ordem/frequencia de output), sem alterar persistencia ou entrada.

## Comportamento antes vs depois

### Antes
- Saida para um aluno consultado:
  - Nota 1
  - Media
  - Nota 2
  - Media

### Depois
- Saida para um aluno consultado:
  - Nota 1
  - Nota 2
  - Media

## Risco e compatibilidade
- Risco funcional: baixo.
- Impacto em API externa: inexistente (script interativo de terminal).
- Compatibilidade: mantida para entradas/saidas esperadas, com melhora na clareza da interface textual.

## Conclusao tecnica
O commit corrige um problema de duplicacao de logs ao reposicionar a impressao da media para fora do loop de iteracao das notas. As demais alteracoes sao de formatacao da experiencia em terminal e limpeza visual do codigo, sem mudanca de regra de negocio.
