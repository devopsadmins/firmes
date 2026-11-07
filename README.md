# HOMENS

Projeto do **ministério de homens**, criado em 07/11/2026.

## O que é
**Firmes** é um site de estudo para homens cristãos, no ar em **https://homens.igrejareformada.app**. Ele tem três partes:
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

Para publicar, rode `vercel deploy --prod --scope eolimabr` na raiz do repositório. O projeto `firmes` (time SLC) já tem a raiz em `site`. O deploy automático a cada push depende de a Vercel ter acesso à conta `devopsadmins` no GitHub.

## Regras
- Os livros são obras protegidas, então não se copiam trechos deles. O material é autoral e indica o capítulo para leitura.
- O devocional do Legendário também não entra no site: é texto de outro autor.
- Os versículos usam a Almeida Revista e Atualizada (ARA). Confira na Bíblia antes de publicar.
- As imagens são geradas com `gerar_imagem`.
- O visual segue o design system do igrejareformada.app (`igreja-reformada/site-v2/landing.blade.php`). Os tokens estão em `site/src/styles/global.css`.

## Andamento
- [x] Semanas 1 a 12: devocional (60 dias), 12 lições e 12 encontros (rascunho, falta conferir com os livros)
- [x] Publicado na Vercel, projeto `firmes` (time SLC), em https://firmes-nu.vercel.app (07/11/2026)
- [x] Design system do igrejareformada.app aplicado: tokens, Figtree e Source Serif 4, logos e componentes
- [x] Domínio homens.igrejareformada.app na Vercel (CNAME sem proxy), no ar em 07/11/2026
- [x] Projeto antigo do Cloudflare Pages apagado
