В репозитории размещается код создаваемого виджета банковских операций клиента. Для проверки функций нужно разместить файлы в среде интепретатора Python, указать вызовы в файле main.

Реализованные методы:

filter_by_state - принимает список словарей и значение для ключа state, возвращает новый список словарей, отфильтрованный по state
sort_by_date - ринимает список словарей и параметр сортировки, возвращает новый список, отсортированный по дате (date)
get_mask_card_number - принимает на вход номер карты в виде числа и возвращает маску номера по правилу
get_mask_account - принимает на вход номер счета в виде числа и возвращает маску номера по правилу

Добавлен пакет с тестовыми модулями:

 - test_account
 - test_card_number
 - test_get_date
 - test_processing

Покрытие тестами составляет 92%.

Добавлен новый модуль generators с функциями:
 - filter_by_currency
 - transaction_descriptions
 - card_number_generator

Примеры использования функций:

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)

Созданы тесты для новых функций
