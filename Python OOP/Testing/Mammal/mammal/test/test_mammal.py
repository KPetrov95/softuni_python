from unittest import TestCase, main
from project.mammal import Mammal

class MammalTests(TestCase):
    def setUp(self):
        self.test_mammal = Mammal("Pencho", "test_type", "test_sound")

    def test_init_and_get_kingdom(self):
        self.assertEqual("Pencho", self.test_mammal.name)
        self.assertEqual("test_type", self.test_mammal.type)
        self.assertEqual("test_sound", self.test_mammal.sound)
        self.assertEqual("animals", self.test_mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Pencho makes test_sound", self.test_mammal.make_sound())

    def test_info(self):
        self.assertEqual("Pencho is of type test_type", self.test_mammal.info())



if __name__ == '__main__':
    main()