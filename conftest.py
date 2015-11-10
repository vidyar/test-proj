def pytest_generate_tests(metafunc):
    metafunc.parametrize("n", range(1, 40 + 1))
