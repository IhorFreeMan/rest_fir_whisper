# rest_for_whisper
**Аудіофайловий аплікаційний сервер**
Цей проект є прикладом реалізації серверної аплікації, яка дозволяє користувачам завантажувати аудіофайли, обробляти їх та отримувати результат у вигляді тексту. Додатково, процес обробки аудіофайлів реалізовано асинхронно за допомогою Celery, що забезпечує швидке та ефективне виконання.

**Основна функціональність**
Завантаження аудіофайлів: Користувачі можуть завантажувати аудіофайли на сервер через API.

Асинхронна обробка аудіофайлів: Після завантаження, аудіофайли обробляються асинхронно за допомогою Celery. Обробка включає конвертацію аудіо в текст за допомогою модулю Whisper.

Отримання статусу обробки: Користувачі можуть запитувати сервер про статус обробки конкретного аудіофайлу. Якщо обробка завершена, вони отримають текстовий результат.

**Як використовувати**
Завантажте аудіофайл на сервер за допомогою POST-запиту на /upload/. Відповідь містить ідентифікатор завантаженого файлу та початковий статус "processing".

Запитайте сервер про статус обробки аудіофайлу за допомогою GET-запиту на /status/<file_id>/. Якщо статус - "processing", повторіть запит пізніше. Якщо статус - "processed", відповідь містить текстовий результат обробки.

**Технології**
Django: Використовується для створення веб-серверу та реалізації API.
Celery: Використовується для асинхронної обробки аудіофайлів.
Whisper: Модуль для обробки аудіофайлів та конвертації в текст.

**Інсталяція та запуск**
Клонуйте репозиторій: git clone <URL репозиторію>
Встановіть необхідні залежності: pip install -r requirements.txt
Запустіть сервер: python manage.py runserver
Висновок
Цей проект демонструє, як реалізувати асинхронну обробку аудіофайлів та використання Celery для покращення продуктивності сервера. Його можна використовувати як основу для подібних проектів з обробки медіафайлів.

Зауваження: Будь ласка, переконайтеся, що ви встановили та налаштували необхідні бібліотеки
