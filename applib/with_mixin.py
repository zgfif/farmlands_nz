from typing import Protocol, TypeVar, runtime_checkable


@runtime_checkable
class Closable(Protocol):
    def close(self) -> None:
        ...



T = TypeVar('T', bound='Closable')



class WithMixin:
    def __enter__(self: T) -> T:
        """
        Enter context manager.
        """
        return self



    def __exit__(self: Closable, exc_type, exc_val, exc_tb) -> None:
        """
        Exit context manager.
        """
        if hasattr(self, 'close') and callable(self.close):
            self.close()
