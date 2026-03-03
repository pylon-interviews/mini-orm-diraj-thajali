import typing


# TODO: implement the query builder here

class ORM:
    pass

############ TESTING CODE BELOW #########################

o = ORM()

print("Running tests...")

# Note: Uncomment the tests as you get them to pass
#
# The later tests won't pass the typechecker until they're implemented.
#
TEST_CASES = [
    lambda: {
        "query": o.table("users"),
        "expected": "SELECT * FROM users;"
    },
    # lambda: {
    #     "query": o.table("users").select("id", "email"),
    #     "expected": "SELECT id, email FROM users;",
    # },
    # lambda: {
    #     "query": o.table("products").select("id", "upc", "volume").where(
    #         o.cond("volume", ">", 300),
    #         o.cond("upc", "=", "1337"),
    #     ),
    #     "expected": "SELECT id, upc, volume FROM products WHERE volume > 300 AND upc = '1337';",
    # },
    # lambda: {
    #     "query": o.table("products").select("product_id", "price").alias("p"),
    #     "expected": "SELECT p.product_id, p.price FROM products p;",
    # },
    # lambda: {
    #     users = o.table("users").select("user_id", "email").alias("u")
    #     loan_apps = o.table("applications").select("loan_id").alias("app")
    #     return {
    #         "query": users.join(loan_apps, using="user_id"),
    #         "expected": "SELECT u.user_id, u.email, app.loan_id FROM users u JOIN applications app USING user_id;"
    #     }
    # },
    # lambda: {
    #     users = o.table("users").select("user_id", "email").alias("u").where(o.cond("user_id", "=", "user_123"))
    #     orders = o.table("orders").select("order_id", "total").alias("o").where(o.cond("total", ">", 1000))
    #     return {
    #         "query": users.join(orders, using="user_id"),
    #         "expected": "SELECT user_id, u.email, o.order_id, o.total FROM users u JOIN orders o USING user_id WHERE user_id = 'user_123' AND o.total > 1000;",
    #     }
    # },
]


def string_assert(test_num: int, obj: typing.Any, expected: str) -> None:
    if expected != obj.render():
        print("Strings did not match!")
        print(f"EXPECTED: {expected}")
        print(f"OBTAINED: {obj.render()}")
        print("Object:", obj)
        raise AssertionError(f"Test #{test_num} failed")


for index, test_case in enumerate(TEST_CASES):
    test_result = test_case()
    query = test_result["query"]
    expected = test_result["expected"]
    string_assert(index, query, expected)
    print(f"Test #{index + 1} passed.")

print("All tests passed :)")
