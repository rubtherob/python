def add_sale(args):
    with open('bakery.csv', 'a', encoding='utf-8') as add:
        add.write(str(args)+'\n')