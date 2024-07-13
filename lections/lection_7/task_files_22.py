text = ['readable content of a page when looking at its layout. The point of',
        'using Lorem Ipsum is that it has a more-or-less normal distribution',
        'of letters, as opposed to using "Content here, content here",',]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell())  # ValueError: I/O operation on closed file.
