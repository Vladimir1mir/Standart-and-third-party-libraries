from pprint import pprint

def introspection_info(obj):
    # Тип объекта.
    type_obj = obj.__class__.__name__

    # Атрибуты объекта.
    attributes = [attr for attr in dir(obj) if not attr.startswith('__')]

    # Методы объекта.
    methods = [method for method in dir(obj) if callable(getattr(obj, method))
               and not method.startswith('__')]

    # Модуль к которому принадлежит объект.
    module = obj.__class__.__module__

    # Возвращаю словарь с данными об объекте включающий все информацию.
    dict_info = {
        'type': type_obj,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return dict_info


# Пример работы:
number_info = introspection_info(42)
pprint(number_info)

# Пример работы с другим типом объекта
list_info = introspection_info([1, 2, 3])
pprint(list_info)


# Пример работы функции ссвоим классом
class MyClass:
    def __init__(self):
        self.attribute = 'value'

    def test(self):
        pass


custom_info = introspection_info(MyClass())
pprint(custom_info)
