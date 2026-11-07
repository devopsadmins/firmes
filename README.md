# HOMENS

Projeto do **ministério de homens**, criado em 07/11/2026.

## O que é
**Firmes** é um site de estudo para homens cristãos, que vai ficar em **homens.igrejareformada.app** (ainda não publicado). Ele tem três partes:
- **Devocional diário:** 12 semanas, de segunda a sexta (60 dias).
- **Escola Dominical:** uma lição por semana, com esboço, perguntas e plano de aula de 45 minutos, pronta para imprimir.
- **Grupos de homens:** roteiro de encontro de 60 minutos por semana, para Legendários, homens congregacionais ou células.

O estudo se baseia em dois livros:
- **"Não se desculpe por ser homem"**, de Alexandro Claudino. É o livro principal: [ficha](referencia/nao-se-desculpe.md).
- **"Seja Homem"**, de Telmo Martinello (Vida). É a leitura complementar: [ficha](referencia/seja-homem.md).

## Onde está cada coisa
- `site/`: o site, feito em Astro e estático.
- `site/conteudo/semanas/NN.toml`: uma semana por arquivo, com os 5 dias (`[[dia]]`), a lição (`[ebd]`) e o encontro (`[grupo]`).
- `site/conteudo/plano.toml`: o tema, o pilar e os capítulos de cada uma das 12 semanas.
- `site/conteudo/livros.toml`: o sumário dos livros e em que semana entra cada capítulo.
- `referencia/`: fotos dos livros e o [material do Legendários](referencia/legendarios.md), com os versículos que não devem ser repetidos.

Para ver o site e para gerar a versão final:
```bash
npm --prefix ~/projetos/HOMENS/site run dev
```

```bash
npm --prefix ~/projetos/HOMENS/site run build
```

O resultado do build vai para `site/dist`.

Para publicar, é envio direto com `wrangler pages deploy` no projeto `firmes`: o Pages ainda não está ligado ao GitHub. Rode o comando a partir de uma pasta **fora** de `site/`, com uma cópia do `dist`, porque o Wrangler 4 converte projetos Astro para Workers por conta própria.

## Regras
- Os livros são obras protegidas, então não se copiam trechos deles. O material é autoral e indica o capítulo para leitura.
- O devocional do Legendário também não entra no site: é texto de outro autor.
- Os versículos usam a Almeida Revista e Atualizada (ARA). Confira na Bíblia antes de publicar.
- As imagens são geradas com `gerar_imagem`.

## Andamento
- [x] Semanas 1 e 2: devocional, lição e encontro (rascunho, falta conferir com os livros)
- [ ] Semanas 3 a 12
- [x] Publicado no Cloudflare Pages, projeto `firmes`, em https://firmes.pages.dev (07/11/2026)
- [ ] Domínio homens.igrejareformada.app: já ligado ao projeto, falta o CNAME `homens` → `firmes.pages.dev` no DNS
