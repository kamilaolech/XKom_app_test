import unittest

from Tests.LoginTest_positive import TestLogin_positive
from Tests.LoginTest_negative import TestLogin_negative
from Tests.PriceSumTest_positive import TestPriceSum_positive

login_test_positive = unittest.TestLoader().loadTestsFromTestCase(TestLogin_positive)
login_test_negative = unittest.TestLoader().loadTestsFromTestCase(TestLogin_negative)
pricesum_test_positive = unittest.TestLoader().loadTestsFromTestCase(TestPriceSum_positive)

test_suite = unittest.TestSuite([login_test_positive, login_test_negative, pricesum_test_positive])

unittest.TextTestRunner(verbosity=2).run(test_suite)
