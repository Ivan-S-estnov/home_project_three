from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n")
                    raise e
                else:
                    print(f"Ошибка: {e}")

            return result

        return wrapper

    return decorator


@log("mylog.txt")
def my_function(x: Any, y: Any) -> Any:
    return x / y


print(my_function(28, 7))
