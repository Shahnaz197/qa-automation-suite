# BUG-001: Cart test intermittently reads inventory items instead of cart items

| Field | Value |
|-------|-------|
| Reported by | Shahnaz |
| Date | 2026-11-03 |
| Environment | GitHub Actions (ubuntu-latest), Chromium, Python 3.12, SauceDemo |
| Severity | Medium (test reliability, not a product defect) |
| Priority | High (blocks a green CI run) |
| Status | Fixed |

## Description
`test_cart_contains_selected_items` passed on the local machine but failed in CI. The test read item names before the browser had navigated to the cart page, so it picked up all 6 product names from the inventory page.

## Steps to reproduce
1. Run the suite in CI (faster, different timing than a local machine).
2. The test adds two items and clicks the cart icon.
3. `item_names()` runs immediately after the click.

## Expected result
Only the 2 items in the cart are returned.

## Actual result
```
Left contains 4 more items, first extra item: 'Sauce Labs Bolt T-Shirt'
```
All 6 inventory item names were returned.

## Root cause
`all_inner_texts()` reads the page as it is at that moment and does not wait for navigation. The locator `.inventory_item_name` also matched items on the inventory page.

## Fix
In `CartPage.item_names()`: wait for `.cart_item` (only exists on the cart page) and scope the locator to `.cart_item .inventory_item_name`.

## Notes
Intermittent, depending on machine speed. The same weakness was found earlier in `item_count()` on the inventory page. Rule applied afterwards: always wait on page state instead of reading immediately after an action.
