# Devocional diário do ministério de homens: plano

O devocional dura **12 semanas, com 5 dias por semana (segunda a sexta), 60 devocionais no total**.
Cada semana acompanha um capítulo do livro-base ([../referencia/livro.md](../referencia/livro.md)).
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

| Sem. | Capítulo (págs.) | Pilar | Tema da semana |
|---|---|---|---|
| 1 | Introdução + O Homem que Deus Imaginou (14–45) | Caráter | Identidade: imagem de Deus antes de qualquer papel |
| 2 | Desígnios e Destinos (46–69) | Fé | Propósito e chamado |
| 3 | A Castração dos Homens (70–101) | Coragem | Passividade, omissão e o peso de se posicionar |
| 4 | O Homem do Céu (102–129) | Fé | Cristo como modelo de homem |
| 5 | Amor, Casamento e Legado (130–155) | Legado | Amar como Cristo amou a igreja |
| 6 | As Batalhas Secretas do Homem (156–181) | Caráter | Pecado escondido, confissão e prestação de contas |
| 7 | A Morte está a um Toque (182–207) | Caráter | Pureza sexual e a tela |
| 8 | Uma Vida Digna de ser Contada (208–233) | Legado | Trabalho, tempo e a história que fica |
| 9 | Paternidade e Amizades que Transformam (234–259) | Liderança | Ser pai, ter irmãos de batalha |
| 10 | A Guerra Invisível (260–283) | Coragem | Batalha espiritual e a armadura de Deus |
| 11 | A Disciplina dos Homens Extraordinários (284–309) | Liderança | Hábitos: oração, Palavra, corpo, dinheiro |
| 12 | Resoluções de um Homem Inabalável + Conclusão (310–fim) | Legado | Compromissos para a vida inteira |

O tema de cada semana foi deduzido do título do capítulo. **Depois de ler o capítulo,
confira o tema** e ajuste antes de escrever aquela semana.

## Como gerar

O conteúdo fica em `semanas/NN.toml`, um arquivo por semana. Para gerar a página, rode:

```bash
python3 ~/projetos/HOMENS/devocional/gerar.py
```

O comando gera `devocional.html`, que funciona no celular e no tema escuro e guarda as respostas só no navegador.

## Andamento

- [x] Semana 1, rascunho: falta conferir com o capítulo e os versículos
- [ ] Semanas 2 a 12
