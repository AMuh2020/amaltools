from django.test import SimpleTestCase

from .functions import binaryToDecimalFunction, binaryToHexadecimalFunction, decimalToBinaryFunction, zeckendorf_representation_function, text_binary
# Create your tests here.

class ConverterTestCase(SimpleTestCase):
    def testBinaryToDecimal (self):
        self.assertEqual(binaryToDecimalFunction.binToDec("1"), 1)
        self.assertEqual(binaryToDecimalFunction.binToDec("0"), 0)
        self.assertEqual(binaryToDecimalFunction.binToDec("101010"), 42)
    
    def testBinaryToHexadecimal (self):
        self.assertEqual(binaryToHexadecimalFunction.binToHex("1"), "1")
        self.assertEqual(binaryToHexadecimalFunction.binToHex("0"), "0")
        self.assertEqual(binaryToHexadecimalFunction.binToHex("101010"), "2A")

    # sends a get request to all urls in app and checks for 200 response
    # def testVisit_all (self):
    #     # https://amaltools.com/tools/bintodec/
    #     # https://amaltools.com/tools/dectobin/
    #     # https://amaltools.com/tools/bintohex/
    #     # https://amaltools.com/tools/zeckendorf/
    #     # https://amaltools.com/tools/bintotext/
    #     # https://amaltools.com/tools/texttobin/
    #     # https://amaltools.com/tools/integertotext/
    #     self.assertEqual(self.client.get("/tools/bintodec/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/dectobin/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/bintohex/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/zeckendorf/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/bintotext/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/texttobin/").status_code, 200)
    #     self.assertEqual(self.client.get("/tools/integertotext/").status_code, 200)
    #     # print("all urls visited successfully")