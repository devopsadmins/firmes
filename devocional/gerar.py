#!/usr/bin/env python3
"""Gera devocional.html a partir de semanas/NN.toml (um arquivo por semana, 5 dias cada)."""
import html
import tomllib
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TOTAL = 60  # 12 semanas x 5 dias
e = html.escape


def ler_semanas():
    semanas = []
    for p in sorted((AQUI / "semanas").glob("*.toml")):
        s = tomllib.loads(p.read_text())
        assert len(s["dia"]) <= 5, f"{p.name}: mais de 5 dias"
        semanas.append(s)
    return semanas


def dia_html(n, d):
    did = f"d{n:02d}"
    texto = "".join(f"<p>{e(t)}</p>" for t in d["texto"])
    perguntas = "".join(f"<li>{e(q)}</li>" for q in d["perguntas"])
    return f"""
  <article id="{did}">
    <div class="num">DIA {n:02d}</div>
    <h2>{e(d['titulo'])}</h2>
    <blockquote class="verse">{e(d['versiculo'])}<cite>{e(d['referencia'])} · ARA</cite></blockquote>
    <div class="body">{texto}</div>
    <div><h3>Aplicação prática</h3><ol class="questions">{perguntas}</ol></div>
    <div class="challenge"><h3>Desafio do dia</h3><p>{e(d['desafio'])}</p></div>
    <div class="prayer"><h3>Oração</h3><p>{e(d['oracao'])}</p></div>
    <div class="answer"><label for="r{did}">{e(d['resposta'])}</label><textarea id="r{did}" data-key="{did}"></textarea></div>
    <p class="reading">Leitura do livro: {e(d['leitura'])}</p>
  </article>
  <hr>"""


def gerar():
    semanas = ler_semanas()
    prontos, blocos = {}, []
    for s in semanas:
        comp = f'\n    <p class="reading">Leitura complementar (opcional): {e(s["complementar"])}</p>' if s.get("complementar") else ""
        blocos.append(f"""
  <section class="week" id="s{s['semana']:02d}">
    <div class="eyebrow">Semana {s['semana']} · {e(s['pilar'])}</div>
    <h2>{e(s['titulo'])}</h2>
    <p>{e(s['capitulo'])}</p>{comp}
  </section>""")
        for i, d in enumerate(s["dia"]):
            n = (s["semana"] - 1) * 5 + i + 1
            prontos[n] = d["titulo"]
            blocos.append(dia_html(n, d))
    trilha = "".join(
        f'<a href="#d{n:02d}" title="{n:02d} · {e(prontos[n])}">{n:02d}</a>' if n in prontos
        else f'<span aria-label="Dia {n:02d} ainda não publicado">{n:02d}</span>'
        for n in range(1, TOTAL + 1)
    )
    css = (AQUI / "estilo.css").read_text()
    pagina = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Homem sem desculpas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
{css}
</style></head><body>
<div class="wrap">
  <header>
    <div class="eyebrow">Ministério de homens · Devocional diário</div>
    <h1>Homem sem desculpas</h1>
    <p class="lede">Doze semanas, de segunda a sexta, acompanhando o livro “Não se desculpe por ser homem”, de Alexandro Claudino, com leitura complementar de “Seja Homem”, de Telmo Martinello. Cada dia traz um versículo, uma reflexão curta, perguntas, o desafio do dia e espaço para a sua resposta.</p>
    <nav class="trail" aria-label="Dias do devocional">{trilha}</nav>
    <p class="trail-note">{len(prontos)} de {TOTAL} dias publicados. Os quadros vazios chegam nas próximas semanas.</p>
  </header>
{''.join(blocos)}
  <footer>Os textos são do ministério e não reproduzem os livros: leia os capítulos indicados. Versículos na Almeida Revista e Atualizada (ARA). As respostas ficam salvas só neste navegador e não são enviadas a ninguém.</footer>
</div>
<script>
document.querySelectorAll('textarea[data-key]').forEach(function (el) {{
  var key = 'homens:' + el.dataset.key;
  try {{ var v = localStorage.getItem(key); if (v) el.value = v; }} catch (err) {{}}
  var note = document.createElement('small');
  el.after(note);
  el.addEventListener('input', function () {{
    try {{ localStorage.setItem(key, el.value); note.textContent = 'Salvo neste navegador.'; }}
    catch (err) {{ note.textContent = 'Não deu para salvar aqui. Copie o texto antes de sair.'; }}
  }});
}});
</script>
</body></html>
"""
    (AQUI / "devocional.html").write_text(pagina)
    print(f"devocional.html: {len(prontos)} de {TOTAL} dias")


if __name__ == "__main__":
    gerar()
