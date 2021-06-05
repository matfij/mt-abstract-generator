from abc import abstractmethod
from typing import List, Tuple

from core.models import ResultPageModel, GenerateAbstractParams


class SpiderContract:
    '''Spicifies requirements for any web spider component facade'''
    
    @abstractmethod
    def get_related_pages(self, phrase: str, page_number: int):
        '''This method must update the StateManager'''
        pass


class PageProcessorContract:
    '''Spicifies requirements for any page processor component facade'''
    
    @abstractmethod
    def clean_content(self, pages: List[ResultPageModel]) -> List[ResultPageModel]:
        pass


class PageRatingContract:
    '''Spicifies requirements for any page rating component facade'''
    
    @abstractmethod
    def get_best_pages(self, pages: List[ResultPageModel]) -> List[ResultPageModel]:
        pass


class AbstractGeneratorContract:
    '''Spicifies requirements for any abstract generator component facade'''
    
    @abstractmethod
    def generate_abstract(self, params: GenerateAbstractParams, corpus: str) -> Tuple[str, str]:
        pass
