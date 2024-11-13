## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 78% (отчет: `file:///Users/aidarshir/Diplom%20/Diplom_1/tests/htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам.`test_bun.py`, `test_burger.py`, `test_database.py`, `test_ingredient.py` и `__init__.py`

### Запуск автотестов

**Установка зависимостей**

> `$ pip3 install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
