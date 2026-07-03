import random
import time
import requests

# настройки
wb_token = "ВАШ_API_ТОКЕН_WILDBERRIES"

# база готовых ответов по оценкам
templates = {
    5: [
        "спасибо за отличную оценку! рады, что вам понравилось.",
        "благодарим за покупку! пользуйтесь с удовольствием.",
        "огромное спасибо за отзыв! ваш выбор очень важен для нас.",
    ],
    4: [
        "спасибо за отзыв! будем стараться стать еще лучше.",
        "благодарим за покупку и обратную связь! рады помочь.",
    ],
    3: [
        "спасибо за отзыв. нам жаль, что товар не полностью оправдал ожидания.",
        "приносим извинения. передали ваш отзыв в отдел качества.",
    ],
    2: [
        "извините за неудобства. свяжитесь с нами для решения проблемы.",
        "нам очень жаль. мы обязательно проверим эту партию товара.",
    ],
    1: [
        "приносим глубокие извинения. хотим исправить ситуацию, свяжитесь с нами.",
        "очень жаль, что так вышло. передали информацию на производство.",
    ],
}


def get_unanswered_reviews():
    # получение новых отзывов
    url = "https://wildberries.ru"
    headers = {"Authorization": wb_token}
    params = {"isAnswered": "false", "take": 10, "skip": 0}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json().get("data", {}).get("feedbacks", [])
        return []
    except Exception:
        return []


def send_answer(review_id, answer_text):
    # отправка ответа на вб
    url = "https://wildberries.ru"
    headers = {"Authorization": wb_token}
    payload = {"id": review_id, "text": answer_text}

    try:
        response = requests.patch(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200
    except Exception:
        return False


def main():
    # главный цикл работы
    while True:
        reviews = get_unanswered_reviews()

        if not reviews:
            # пауза 5 минут если нет отзывов
            time.sleep(300)
            continue

        for review in reviews:
            review_id = review.get("id")
            valuation = review.get("productValuation")

            # выбор случайного ответа по оценке
            if valuation in templates:
                answer = random.choice(templates[valuation])
            else:
                answer = "спасибо за ваш отзыв!"

            # отправка
            send_answer(review_id, answer)
            # пауза между ответами
            time.sleep(3)

        # пауза перед новой проверкой
        time.sleep(60)


if __name__ == "__main__":
    main()
