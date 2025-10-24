def is_valid_email(s: str) -> bool:

    return '@' in s and '.' in s.split('@')[-1] and s.count('@') == 1

print(is_valid_email("justsanchez241@gmail..com"))

print(is_valid_email("stepa180877@gmail.com"))

print(is_valid_email("stepa2007@bigmir.net"))



Разбор: 
1. def is_valid_email(s: str) -> bool: - создаётся функция с именем is_valid_email, которая принимает строку s (предположительно email) и возвращает true или false.
2.     return '@' in s and '.' in s.split('@')[-1] and s.count('@') == 1 - результат проверки, все три условия должны быть выполнены. 
3. print(is_valid_email("justsanchez241@gmail..com"))
   print(is_valid_email("stepa180877@gmail.com"))
   print(is_valid_email("stepa2007@bigmir.net")) - выводим почты и смотрим результат true or false 

Источники:

https://www.geeksforgeeks.org/python/check-if-email-address-valid-or-not-in-python/?utm_source=

https://www.pythonexamples.org/python-email-validation/

https://www.codespeedy.com/validate-email-in-python/?utm_source=

https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/?utm_source=

https://www.iditect.com/faq/python/how-to-check-for-valid-email-address-in-python.html?utm_source=