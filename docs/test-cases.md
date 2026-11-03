# Test Cases

## A. Automated test cases

| ID | Area | Scenario | Expected result | Automated test |
|----|------|----------|-----------------|----------------|
| TC-01 | Login | Valid login with standard_user | Lands on inventory page | `test_valid_login_lands_on_inventory` |
| TC-02 | Login | Login with locked_out_user | Error says user is locked out | `test_locked_out_user_sees_error` |
| TC-03 | Login | Wrong password | "do not match" error shown | `test_invalid_credentials_show_error` |
| TC-04 | Login | Empty username | "Username is required" | `test_invalid_credentials_show_error` |
| TC-05 | Login | Empty password | "Password is required" | `test_invalid_credentials_show_error` |
| TC-06 | Inventory | Open inventory after login | 6 products displayed | `test_inventory_shows_six_products` |
| TC-07 | Cart | Add then remove an item | Badge shows 1, then disappears | `test_add_and_remove_item_updates_badge` |
| TC-08 | Cart | Add two items and open cart | Cart lists exactly those two | `test_cart_contains_selected_items` |
| TC-09 | Inventory | Sort price low to high | Prices in ascending order | `test_sort_price_low_to_high` |
| TC-10 | Checkout | Complete a full purchase | "Thank you for your order" | `test_full_checkout_flow` |
| TC-11 | Checkout | Leave first name empty | "First Name is required" | `test_checkout_requires_first_name` |
| TC-12 | API | GET /posts/1 | 200, body has userId, id, title, body | `test_get_single_post` |
| TC-13 | API | GET /posts?userId=1 | 200, 10 posts, all userId 1 | `test_filter_posts_by_user` |
| TC-14 | API | POST /posts | 201, response has id and title | `test_create_post_returns_201` |
| TC-15 | API | PUT /posts/1 | 200, title updated | `test_update_post` |
| TC-16 | API | DELETE /posts/1 | 200 | `test_delete_post` |
| TC-17 | API | GET /posts/99999 | 404 | `test_unknown_post_returns_404` |
| TC-18 | API | GET /posts response time | Under 2 seconds | `test_response_time_under_two_seconds` |

## B. Manual / exploratory test ideas (to run and record results)

| ID | Charter | What to look for | Result |
|----|---------|------------------|--------|
| EX-01 | Login with unusual input (spaces, very long text, special characters) | Crashes, unhelpful errors, input not trimmed | _to fill_ |
| EX-02 | Browser Back/Forward during checkout | Lost cart, wrong page state | _to fill_ |
| EX-03 | Open /inventory.html directly without logging in | Access should be blocked | _to fill_ |
| EX-04 | Refresh the page with items in cart | Cart contents persist or not | _to fill_ |
| EX-05 | Resize the window to a phone width | Layout breaks, hidden buttons | _to fill_ |

Run each charter for about 15 minutes, write down what you saw, and raise a bug report for anything wrong.
