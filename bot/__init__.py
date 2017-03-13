#-*- coding: utf-8 -*-

__all__ = (
    '__version__',
    '__author_vk_id__',
    '__author__',
    '__help__'
    )

__version__ = '0.0.3'
__author_vk_id__ = 180850898
__author__ = 'Eugene Ershov - https://vk.com/id%d' % __author_vk_id__

__help__ = '''
Версия: {v}

Я умею:
*Говорить то, что вы попросите
(/say ... |/скажи ... )
*Производить математические операции
(/calculate ... |/посчитай ... ) =
*Проверять, простое ли число
(/prime ... |/простое ... ) %
*Вызывать помощь
(/help |/помощь ) ?


Автор: {author}

В конце моих сообщений ставится знак верхней кавычки
'''.format(\
    v = __version__, author = __author__
)
