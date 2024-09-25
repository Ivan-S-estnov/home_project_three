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
                    print("my_function ok")
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my_function ok\n")

            except Exception as e:
                print(f"Ошибка: {e}")
                raise e
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"my_function error: {e} Inputs: {args}, {kwargs}")

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    return x / y


print(my_function(6, 1))
