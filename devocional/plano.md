# Devocional diário do ministério de homens: plano

O devocional dura **12 semanas, com 5 dias por semana (segunda a sexta), 60 devocionais no total**.
Cada semana segue um capítulo do livro principal, **Não se desculpe por ser homem**
([../referencia/nao-se-desculpe.md](../referencia/nao-se-desculpe.md)). A leitura complementar vem de
**Seja Homem** ([../referencia/seja-homem.md](../referencia/seja-homem.md)), com 1 ou 2 capítulos curtos por semana.
A introdução entra na semana 1 e a conclusão na semana 12. Assim, a leitura fica em cerca de
5 páginas por dia, junto com o devocional. Sábado e domingo ficam livres para alcançar quem atrasou e para o encontro do grupo.

Cada dia tem:

1. Número e título.
2. Um versículo curto, na Almeida Revista e Atualizada (ARA).
3. Um texto autoral de 2 a 3 parágrafos, sem copiar o livro.
4. Duas perguntas de aplicação.
5. O desafio do dia.
6. Uma oração em forma de roteiro.
7. Um campo de resposta, salvo só no aparelho.
8. A leitura do livro daquele dia (páginas).

| Sem. | Não se desculpe (págs.) | Seja Homem: complementar (págs.) | Pilar | Tema da semana |
|---|---|---|---|---|
| 1 | Introdução + O Homem que Deus Imaginou (14–45) | Introdução (11–12) + Homens resolvidos (143–150) | Caráter | Identidade: imagem de Deus antes de qualquer papel |
| 2 | Desígnios e Destinos (46–69) | Decida (37–46) + Encontre o favor do rei (71–82) | Fé | Propósito e chamado |
| 3 | A Castração dos Homens (70–101) | Acabe com Acabe (13–24) + Desistir não é uma opção (59–70) | Coragem | Passividade, omissão e o peso de se posicionar |
| 4 | O Homem do Céu (102–129) | Desconfie de quem não manca (47–58) | Fé | Cristo como modelo; o encontro que quebra o homem |
| 5 | Amor, Casamento e Legado (130–155) | Lições de Boaz (151–160) + Homem, coloque a sua casa em ordem (91–98) | Legado | Amar como Cristo amou a igreja |
| 6 | As Batalhas Secretas do Homem (156–181) | Homens curados, famílias curadas (121–132) | Caráter | Pecado escondido, confissão e prestação de contas |
| 7 | A Morte está a um Toque (182–207) | Protegendo os muros baixos (189–200) | Caráter | Pureza sexual e a tela |
| 8 | Uma Vida Digna de ser Contada (208–233) | Crescer dói (25–36) + Quando a fatura chega (201–210) | Legado | Trabalho, tempo, consequências e a história que fica |
| 9 | Paternidade e Amizades que Transformam (234–259) | Paternidade (173–188) + Homem, um conselho para você (111–120) | Liderança | Ser pai, ter irmãos de batalha |
| 10 | A Guerra Invisível (260–283) | Homem, coloque sua armadura (83–90) + Homem, pegue a sua espada (99–110) | Coragem | Batalha espiritual e a armadura de Deus |
| 11 | A Disciplina dos Homens Extraordinários (284–309) | Mente de governo (161–172) + Sabedoria para governar (211–220) | Liderança | Hábitos e governo de si: oração, Palavra, corpo, dinheiro |
| 12 | Resoluções de um Homem Inabalável + Conclusão (310–fim) | Homens geracionais (133–142) + Conclusão (221–fim) | Legado | Compromissos para a vida inteira |

Os 19 capítulos do Seja Homem entram uma vez cada. A leitura complementar é opcional e
aparece no começo de cada semana na página. Quem tiver só um dos livros acompanha do mesmo jeito.

Os temas e o encaixe do Seja Homem foram deduzidos dos títulos dos capítulos. **Depois de ler os capítulos,
confira o tema e o encaixe** e ajuste antes de escrever aquela semana.

## Como gerar

O conteúdo fica em `semanas/NN.toml`, um arquivo por semana. Para gerar a página, rode:

```bash
python3 ~/projetos/HOMENS/devocional/gerar.py
```

O comando gera `devocional.html`, que funciona no celular e no tema escuro e guarda as respostas só no navegador.

## Andamento

- [x] Semana 1, rascunho: falta conferir com o capítulo e os versículos
- [x] Semana 2, rascunho: falta conferir com o capítulo e os versículos
- [ ] Semanas 3 a 12
