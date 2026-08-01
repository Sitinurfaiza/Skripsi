import re

with open('scratch_gen_bab3.txt', 'r', encoding='utf-8') as f:
    tex_bab3 = f.read()

with open(r'd:\PROJECT\Skripsi\Skripsi.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

bab3_start = tex.find(r'\chapter[METODOLOGI PENELITIAN]')
bab4_start = tex.find(r'\chapter[HASIL DAN PEMBAHASAN]')

updated_tex = tex[:bab3_start] + tex_bab3 + '\n\n' + tex[bab4_start:]

with open(r'd:\PROJECT\Skripsi\Skripsi.tex', 'w', encoding='utf-8') as f:
    f.write(updated_tex)

print('Successfully applied BAB 3 from text file!')
