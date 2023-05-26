from src.testcases.testcase1 import textbox_validation
from src.testcases.testcase2 import checkbox_validation


class Elements:
    def testCase_caller(self):
        # Testcase 1
        textbox_validation().textbox_test()
        # Testcase 2
        checkbox_validation().checkbox_test()
