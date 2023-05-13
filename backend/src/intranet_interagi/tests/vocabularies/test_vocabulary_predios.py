from intranet_interagi import PACKAGE_NAME
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabIndustries:

    name = f"{PACKAGE_NAME}.predios"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, portal):
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token",
        [
            "sede",
            "filial-01",
            "filial-02",
            "filial-03",
            "filial-04",
        ],
    )
    def test_token(self, token):
        assert token in [x for x in self.vocab.by_token]
