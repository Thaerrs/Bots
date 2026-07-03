import random
import time

# база готовых ответов по оценкам
templates = {
    5: [
        "Спасибо за отличную оценку! Рады, что вам понравилось.",
        "Благодарим за покупку! Пользуйтесь с удовольствием.",
    ],
    4: ["Спасибо за отзыв! Будем стараться стать еще лучше."],
    3: ["Спасибо за отзыв. Нам жаль, что товар не оправдал ожидания."],
    2: ["Извините за неудобства. Свяжитесь с нами для решения проблемы."],
    1: ["Приносим глубокие извинения. Хотим исправить ситуацию."],
}


def get_fake_reviews():
    # имитация получения новых отзывов из вб
    # генерирует случайный отзыв для проверки
    fake_id = random.randint(1000, 9999)
    fake_valuation = random.randint(1, 5)

    # имитируем, что отзывы приходят не всегда
    if random.choice([True, False]):
        return [{"id": fake_id, "productValuation": fake_valuation}]
    return []


def send_fake_answer(review_id, answer_text):
    # имитация отправки ответа на вб
    # просто выводит результат в консоль
    print(f"[WB API] ответ на отзыв №{review_id} успешно отправлен!")
    return True


def main():
    # главный цикл работы
    print("тестовый запуск бота без подключения к api...")

    for _ in range(5):  # сделаем 5 проверок чтобы не крутить бесконечно
        reviews = get_fake_reviews()

        if not reviews:
            print("новых отзывов нет. ждем...")
            time.sleep(2)
            continue

        for review in reviews:
            review_id = review.get("id")
            valuation = review.get("productValuation")

            print(f"\n[входные данные] пришел отзыв №{review_id} с оценкой {valuation}")

            # выбор шаблона
            if valuation in templates:
                answer = random.choice(templates[valuation])
            else:
                answer = "Спасибо за ваш отзыв!"

            print(f"[логика бота] выбран ответ: '{answer}'")

            # отправка заглушке
            send_fake_answer(review_id, answer)
            time.sleep(1)

        time.sleep(2)

    print("\nтестирование успешно завершено!")


if __name__ == "__main__":
    main()
