# coding: utf-8

from bertalign import Bertalign


def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
    if isinstance(text, list):
        return [t.strip() for t in text]
    elif isinstance(text, str):
        return text.strip()
    else:
        return text


chinois_phrase = read_text_from_file('C:\\Projet_TAL\\Corpus_brut\\chinois.txt')

francais_phrase = read_text_from_file('C:\\Projet_TAL\\Corpus_brut\\francais.txt')

chinois_phrase = clean_text(chinois_phrase)
francais_phrase = clean_text(francais_phrase)

aligner = Bertalign(chinois_phrase, francais_phrase)
aligner.align_sents()
#aligner.print_sents()

filealigne = open("C:\\Projet_TAL\\Corpus_brut\\phrase_aligne.txt", "w", encoding='utf-8')
for align in aligner.result:
    src_line = aligner._get_line(align[0], aligner.src_sents)
    tgt_line = aligner._get_line(align[1], aligner.tgt_sents)
    filealigne.write(f'{src_line}\t{tgt_line}\n')

filealigne.close()

