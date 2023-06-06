

with open('uhan_online.txt', mode='r', encoding='utf8') as online:
    for line in online:
        with open('uhan_offline.txt', mode='r', encoding='utf8') as offline:
            for line_ in offline:
                if line == line_:
                    continue
                else:
                    with open('result.txt', mode='w', encoding='utf8') as result:
                        result.write(f'{line} *^10 {line_}')
