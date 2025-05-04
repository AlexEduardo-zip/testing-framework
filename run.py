from testing_framework.test_loader import TestLoader
from testing_framework.test_runner import TestRunner

from tests.test_testloader import TestLoaderTest

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)