import sys

for line in sys.stdin:
    fname, sentence = line.rstrip('\n').split('\t')
    with open('sent_' + fname + '.txt', 'w') as f:
        f.write(sentence)



