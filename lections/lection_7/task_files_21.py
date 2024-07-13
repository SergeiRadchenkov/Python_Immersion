text = ['readable content of a page when looking at its layout. The point of',
        'using Lorem Ipsum is that it has a more-or-less normal distribution',
        'of letters, as opposed to using "Content here, content here",',]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
