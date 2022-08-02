import wikipedia, re, string

alphabet = string.ascii_lowercase + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.digits

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")



def clean_str(mesage):
    res = mesage.lower()
    res = [c for c in res if c in alphabet]
    return ''.join(res)



def getwiki(s):
    try:
        clear_text = clean_str(s)
        ny = wikipedia.page(clear_text)
        # Получаем первую тысячу символов(можно взять больше)
        wikitext = ny.content[:1000]
        wikilinks = ny.url
        # Разделяем по точкам ( потому что по точкам прозе всего )
        wikimas = wikitext.split('.')
        # Отбрасываем все после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку( можно и без этого но на всякий случай)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        wikitext2 = wikitext2 + '\n\n'
        # Возвращаем текстовую строку
        return wikitext2, wikilinks
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом\n', 'Введите что-нибудь другое\n'


if __name__ == "__main__":
    print(getwiki('Чайнатаун'))
