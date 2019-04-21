#  rplugin/python3/denite/source/deso.py
from .base import Base
# import datetime


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'deso'
        # self.kind = 'word'

    def gather_candidates(self, context):
        candidates = []

        candidates.append({
            'word': 'fuga',
            'abbr': '🦅🦅🦅🦅🦅🦅🦅🦅🦅🦅',
        })

        return candidates
