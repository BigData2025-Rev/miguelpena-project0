import pandas as pd
from abc import ABC, abstractmethod

class IData(ABC):
    @abstractmethod
    def save(self) -> None:
        ...
    @abstractmethod
    def load(self) -> pd.DataFrame:
        ...