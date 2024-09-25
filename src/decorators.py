from fileinput import filename
from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{func.__name__} ok\n")
            except Exception as e:
                print(f"Ошибка: {e}")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n")
                raise e

            return result

        return wrapper

    return decorator


@log("mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    return x / y


print(my_function(2,5))
