// Lê o conteúdo em conteudo/*.toml na hora do build. Nada disso vai para o navegador.
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { parse } from 'smol-toml';

const RAIZ = join(process.cwd(), 'conteudo');
export const TOTAL_DIAS = 60;
export const TOTAL_SEMANAS = 12;

export interface Dia {
  titulo: string; versiculo: string; referencia: string; leitura: string;
  texto: string[]; perguntas: string[]; desafio: string; oracao: string; resposta: string;
}
export interface Ebd {
  titulo: string; texto_base: string; objetivo: string; verdade: string;
  esboco: { ponto: string; referencias: string; explicacao: string }[];
  perguntas: string[]; aplicacao: string; professor: string[];
}
export interface Grupo {
  abertura: string; quebra_gelo: string; leitura: string; conversa: string[];
  desafio: string; oracao: string;
}
export interface Semana {
  semana: number; titulo: string; pilar: string; capitulo: string; complementar?: string;
  resumo: string; dia: Dia[]; ebd?: Ebd; grupo?: Grupo;
}
export interface DiaNumerado extends Dia { n: number; semana: Semana }

export interface Capitulo { titulo: string; pagina: number; semana?: number }
export interface Livro {
  id: string; titulo: string; subtitulo?: string; autor: string; editora?: string;
  papel: string; capitulos: Capitulo[];
}

export function semanas(): Semana[] {
  const dir = join(RAIZ, 'semanas');
  return readdirSync(dir)
    .filter((f) => f.endsWith('.toml'))
    .sort()
    .map((f) => parse(readFileSync(join(dir, f), 'utf8')) as unknown as Semana);
}

export function dias(): DiaNumerado[] {
  return semanas().flatMap((s) =>
    s.dia.map((d, i) => ({ ...d, n: (s.semana - 1) * 5 + i + 1, semana: s })),
  );
}

export function livros(): Livro[] {
  return (parse(readFileSync(join(RAIZ, 'livros.toml'), 'utf8')) as unknown as { livro: Livro[] }).livro;
}

// Plano das 12 semanas: existe antes de o conteúdo de cada semana ser escrito.
export interface PlanoSemana { semana: number; tema: string; pilar: string; principal: string; complementar: string }
export function plano(): PlanoSemana[] {
  return (parse(readFileSync(join(RAIZ, 'plano.toml'), 'utf8')) as unknown as { semana: PlanoSemana[] }).semana;
}

export const dd = (n: number) => String(n).padStart(2, '0');
