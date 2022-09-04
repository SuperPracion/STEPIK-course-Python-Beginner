from random import *

continuation_answer = ['да', 'ага']
answer_options = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
                  'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать'
                  'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
answer = 'да'


def return_answer():
    return choice(answer_options)


while answer in continuation_answer:
    print('Give me your questions')
    input()
    print(return_answer())

    print('Ещё?')
    answer = input().lower()
