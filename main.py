# Задача. Використання замикання для підрахунку кількості викликів
# Створіть функцію, яка використовує замикання для підрахунку кількості викликів. Функція повинна приймати іншу функцію як аргумент та повертати нову функцію, яка обгортає передану функцію. Кожен раз, коли обгорнута функція викликається, лічильник має збільшуватися на одиницю.
# Тести  Щоб здати задачу усі тести повинні бути пройдені.
# Перевірка, чи лічильник правильно враховує кількість викликів функції.
# Додавання ще двох викликів і перевірка лічильника.
# Перевірка, чи функція обгортка повертає значення лічильника.
# Виклик функції з параметрами і перевірка лічильника.

def counter(func):
    count = 0  # Ініціалізуємо лічильник викликів функції

    def wrapper(*args, **kwargs):
        nonlocal count  # Оголошуємо, що будемо використовувати змінну count з зовнішньої області видимості
        count += 1  # Збільшуємо лічильник на 1 при кожному виклику функції
        result = func(*args, **kwargs)  # Викликаємо оригінальну функцію з переданими аргументами і зберігаємо результат
        wrapper.call_count = count  # Оновлюємо значення лічильника викликів у обгортці
        wrapper.last_result = result  # Зберігаємо останній результат виклику функції
        return count  # Повертаємо лічильник при кожному виклику

    wrapper.call_count = count  # Ініціалізуємо початкове значення лічильника викликів у обгортці
    wrapper.last_result = None  # Ініціалізуємо початкове значення останнього результату виклику функції
    return wrapper  # Повертаємо обгортку функції


@counter
def example_function(*args, **kwargs):
    print("Inside the function")  # Виводимо повідомлення при виклику функції
    return args, kwargs  # Повертаємо передані аргументи для демонстрації


@counter
def another_function(x):
    return x * 2  # Повертаємо подвоєне значення переданого аргументу


# Перевірка:
result_1 = example_function()  # Викликаємо example_function без аргументів
print(result_1)  # Виводимо результат виклику (лічильник викликів)
print(example_function.call_count)  # Виводимо поточне значення лічильника викликів

example_function()  # Викликаємо example_function без аргументів
example_function()  # Викликаємо example_function без аргументів
result_2 = example_function()  # Викликаємо example_function без аргументів
print(result_2)  # Виводимо результат виклику (лічильник викликів)
print(example_function.call_count)  # Виводимо поточне значення лічильника викликів

# Виклик функції з параметрами
result_5 = example_function(10, key="value")  # Викликаємо example_function з аргументами
print(result_5)  # Виводимо результат виклику (лічильник викликів)
print(example_function.call_count)  # Виводимо поточне значення лічильника викликів

result_3 = another_function(5)  # Викликаємо another_function з аргументом 5
print(result_3)  # Виводимо результат виклику (лічильник викликів)
print(another_function.last_result)  # Виводимо останній результат виклику функції
print(another_function.call_count)  # Виводимо поточне значення лічильника викликів

another_function(10)  # Викликаємо another_function з аргументом 10
result_4 = another_function(15)  # Викликаємо another_function з аргументом 15
print(result_4)  # Виводимо результат виклику (лічильник викликів)
print(another_function.last_result)  # Виводимо останній результат виклику функції
print(another_function.call_count)  # Виводимо поточне значення лічильника викликів

# Виклик функцій один за одним для тестування лічильника
example_function()  # Викликаємо example_function без аргументів
another_function(5)  # Викликаємо another_function з аргументом 5
example_function()  # Викликаємо example_function без аргументів
another_function(10)  # Викликаємо another_function з аргументом 10

# Перевірка лічильників після додаткових викликів
print(example_function.call_count)  # Виводимо поточне значення лічильника викликів для example_function
print(another_function.call_count)  # Виводимо поточне значення лічильника викликів для another_function
# Виклик функції з параметрами
result_5 = example_function(10, key="value")  # Викликаємо example_function з аргументами
print(result_5)  # Виводимо результат виклику (лічильник викликів)
print(example_function.call_count)  # Виводимо поточне значення лічильника викликів