from testCase.test_login import test_login_with_validAccout, test_login_with_invalidAccout

if __name__ == "__main__":
    print("▶ Running test: valid account")
    test_login_with_validAccout()
    print("✅ Passed: valid account\n")

    print("▶ Running test: invalid account")
    test_login_with_invalidAccout()
    print("✅ Passed: invalid account\n")
