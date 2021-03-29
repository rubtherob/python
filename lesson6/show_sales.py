def show_sales(*args):
    if len(args)==0:
        with open('bakery.csv', 'r', encoding='utf-8') as show:
            for lines in show:
                print(lines.strip())
    elif len(args)==1:
        counter=1
        with open('bakery.csv', 'r', encoding='utf-8') as show:
            for lines in show:
                if counter>=args[0]:
                    print(lines.strip())
                else:
                    counter+=1
    elif len(args)==2:
        counter=1
        with open('bakery.csv', 'r', encoding='utf-8') as show:
            for lines in show:
                if counter>=args[0] and counter<=args[1]:
                    print(lines.strip())
                    counter+=1
                elif counter>=args[1]:
                    break
                else:
                    counter+=1