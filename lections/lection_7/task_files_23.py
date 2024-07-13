last = before = 0
text = ['readable content of a page when looking at its layout. The point of',
        'using Lorem Ipsum is that it has a more-or-less normal distribution',
        'of letters, as opposed to using "Content here, content here",',]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
