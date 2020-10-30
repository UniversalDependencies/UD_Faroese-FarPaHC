import pyconll
import os
import re
import sys


def fix_sent_ids(conll, file_count, total_count):
    lines = conll.split('\n')
    s_id = lines[1]
    x_id = lines[0]
    new_s_id = s_id.split(',')[0]+f',{file_count}.{total_count}'
    new_lines = [new_s_id, x_id] + lines[2:]
    return '\n'.join(new_lines)

input_folder = sys.argv[1]

dev_test_file = '1928.ntacts.rel-bib.conllu'

output_file = f'fo_farpahc-ud-dev.conllu'
print(f'Writing to file: {output_file}')
with open(output_file, 'w+') as f:
    conll = pyconll.iter_from_file(os.path.join(input_folder, dev_test_file))
    sent_count = 0
    for sentence in conll:
        sent_count += 1
        output_conll = fix_sent_ids(sentence.conll(), '', sent_count)
        f.write(output_conll)
        f.write('\n\n')
        if sent_count == 300:
            break

output_file = f'fo_farpahc-ud-test.conllu'
print(f'Writing to file: {output_file}')
with open(output_file, 'w+') as f:
    conll = pyconll.iter_from_file(os.path.join(input_folder, dev_test_file))
    sent_count = 0
    out_sent_count = 0 
    for sentence in conll:
        sent_count += 1
        if sent_count >= 301:
            out_sent_count += 1
            output_conll = fix_sent_ids(sentence.conll(), '', out_sent_count)
            f.write(output_conll)
            f.write('\n\n')


train_file = '1936.ntjohn.rel-bib.conllu'

output_file = f'fo_farpahc-ud-train.conllu'
print(f'Writing to file: {output_file}')
with open(output_file, 'w+') as f:
    sent_count = 0
    conll = pyconll.iter_from_file(os.path.join(input_folder, train_file))
    for sentence in conll:
        sent_count += 1
        output_conll = fix_sent_ids(sentence.conll(), '', sent_count)
        f.write(output_conll)
        f.write('\n\n')