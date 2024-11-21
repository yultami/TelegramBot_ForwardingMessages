from dataclasses import dataclass as datacls


@datacls(eq=False)
class LogicException(Exception):
    @property
    def msg(self) -> str:
        return 'An error has occurred'

    def __str__(self) -> str:
        return self.msg
