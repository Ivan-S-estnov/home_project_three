from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if filename:
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my_function ok")
                        print("my_function ok")

            except Exception as e:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"my_function error: {e} Inputs: {args}, {kwargs}")
                    print(Exception(f"Ошибка: {e}"))
                raise Exception(f"Ошибка: {e}")

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    return x + y


print(my_function(1, 5))
