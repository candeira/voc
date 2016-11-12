from unittest import expectedFailure

from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            print(x.attr)
            print('Done.')
            """)

    def test_init(self):
        self.assertCodeExecution("""
            x = bytes("Ramón de España", 'utf-8')
            print(x)
            """)

        self.assertCodeExecution("""
            x = bytes("Ramón de España", 'latin-1')
            print(x)
            """)

        self.assertCodeExecution("""
            x = byes("Clive James", 'ascii')
            print(x)
            """)

    @expectedFailure
    def test_init_encode_error(self):
        # test with accents can't be encoded with ascii,
        # should raise UnicodeEncodeError
        self.assertCodeExecution("""
            x = bytes("Ramón de España", 'ascii')
            print(x)
            """)

    def test_equality_properly(self):
        # testing something against itself not enough for buffer.Buffer
        # we need two separate values which are equivalent
        # see http://paste.ubuntu.com/23358563/
        self.assertCodeExecution("""
            utf8_ints = bytes([82, 97, 109, 195, 179, 110, 32, 100, 101, 32,
                               69, 115, 112, 97, 195, 177, 97])
            utf8_string = bytes("Ramón de España", "utf-8")
            print(utf8_ints)
            print(utf8_string)
            print(utf8_int == utf8_string)
            """)

    def test_decode(self):
        self.assertCodeExecution("""
            print("Encoded with utf-8")
            x = bytes([82, 97, 109, 195, 179, 110, 32, 100, 101, 32, 69, 115, 112, 97, 195, 177, 97])
            print(x.decode('utf-8'))
            """)

        self.assertCodeExecution("""
            print("Encoded with iso-latin1")
            x = bytes([82, 97, 109, 243, 110, 32, 100, 101, 32, 69, 115, 112, 97, 241, 97])
            print(x.decode('latin-1'))
            """)

        self.assertCodeExecution("""
            print("Encoded with ascii")
            x = b'Clive James'
            print(x.decode('ascii'))
            """)

    @expectedFailure
    def test_decode_error(self):
        self.assertCodeExecution("""
            # encoded with utf_8
            x = bytes([82, 97, 109, 195, 179, 110, 32, 100, 101, 32, 69, 115, 112, 97, 195, 177, 97])
            print(x.decode('ascii'))
            """)

        self.assertCodeExecution("""
            // encoded with latin_1
            x = bytes([82, 97, 109, 243, 110, 32, 100, 101, 32, 69, 115, 112, 97, 241, 97])
            print(x.decode('utf-8'))
            """)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_eq_class',
        'test_eq_frozenset',

        'test_ne_class',
        'test_ne_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_class',
        'test_ge_frozenset',

        'test_gt_class',
        'test_gt_frozenset',

        'test_le_class',
        'test_le_frozenset',

        'test_lt_class',
        'test_lt_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]
