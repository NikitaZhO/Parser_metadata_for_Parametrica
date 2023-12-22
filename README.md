Parser metadata for Parametrica
---

Данная программа обрабатывает методатанные из конфигурации Parametrica и записывает их в файл `metadata.txt`

---
Установка
---

Для работы с данной программой необходимо выполнить следующие действия:

1. Скопировать данный репозиторий себе на компьютер, сделать можно при помощи команды 
    '$ git clone https://github.com/NikitaZhO/Parser_metadata_for_Parametrica.git`
2. Установить необходимые библиотеки
    `$ pip freeze -r requirements.txt`
3. Для запуска используется файл `main.py`

---
Настроки Программы
---

В файле `default_varieble.py` находятся стандартные настройки для программы
* `write_hint = '1'` - Данный параметр отвечает за добавление комментариев к итоговому файлу.
  * `'1'` - Указывает на то, что комментарии включены и в файле будут отображаться, чтобы их отключить введите любой 
  другой символ вместо `1`

* `secret_field = '1'` - Параметр отвечает за отображение секретных полей.
  * `'1'` - Указывает, что отображение секретных полей включено, чтобы их отключить введите любой другой символ вместо `1`

* `rule_field = '1'` - Параметр отвечает за отображение ограничивающих полей.
  * `'1'` - Указывает, что отображение ограничивающих полей включено, чтобы их отключить введите любой другой 
  символ вместо `1`

---

