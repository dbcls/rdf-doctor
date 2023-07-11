import unittest
from doctor.doctor import get_refine_class_uris
from tests.consts import REFINE_CLASS_URIS_FILE_PATH
from pathlib import Path

class TestGetRefineClassUris(unittest.TestCase):

    def test_get_refine_class_uris(self):
        refine_class_uris = get_refine_class_uris(str(Path(__file__).resolve().parent.joinpath(REFINE_CLASS_URIS_FILE_PATH)))
        self.assertEqual(refine_class_uris, [['http://xmlns.com/foaf/0.1#Person', 'http://xmlns.com/foaf/0.1/Person'], \
                                                ['http://xmlns.com/foaf/0.1/PErson', 'http://xmlns.com/foaf/0.1/Person'], \
                                                ['http://xmlns.com/foaf/0.1/Parson', 'http://xmlns.com/foaf/0.1/Person'], \
                                                ['http://xmlns.com/foaf/0.1/PERSON', 'http://xmlns.com/foaf/0.1/Person'], \
                                                ['http://xmlns.com/foaf/0.1#Document', 'http://xmlns.com/foaf/0.1/Document'], \
                                                ['http://xmlns.com/foaf/0.1/Docment', 'http://xmlns.com/foaf/0.1/Document'], \
                                                ['http://xmlns.com/foaf/0.1/DOCUMENT', 'http://xmlns.com/foaf/0.1/Document'], \
                                                ['http://purl.jp/knapsack/resource#KNApSAcKReference  http://purl.org/ontology/bibo/Article']])

if __name__ == "__main__":
    unittest.main()