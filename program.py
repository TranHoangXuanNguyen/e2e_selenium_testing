from testCase.test_login import test_login_with_validAccout, test_login_with_invalidAccout
from testCase.test_add_to_card import test_add_product_to_cart
if __name__ == "__main__":
    print("▶ Running test: valid account")
    test_login_with_validAccout()
    print("✅ Passed: valid account\n")

    print("▶ Running test: invalid account")
    test_login_with_invalidAccout()
    print("✅ Passed: invalid account\n")
    
    print("▶ Running test: add product")
    test_add_product_to_cart()
    print("✅ Passed: add 1 product success \n")

