# CSV Test Cases - Improvements Made

## Issues Fixed

### 1. ✅ Removed Premature "Actual Result" from Manual Tests

**Issue**: Manual-only test cases had "Actual Result" values even though they were never executed.

**Fixed Cases:**
- **TC_LOGIN_07**: Removed actual result - test needs to be run manually with network inspection
- **TC_SIGNUP_03**: Removed actual result - marked as "Not Run"
- **TC_PROD_05**: Removed actual result - marked as "Not Run"
- **TC_PROD_06**: Removed actual result - marked as "Not Run"
- **TC_CART_04**: Removed actual result - marked as "Not Run"
- **TC_CART_06**: Removed actual result - marked as "Not Run"
- **TC_CHECKOUT_03**: Removed actual result - marked as "Not Run"
- **TC_UI_01**: Removed actual result - marked as "Not Run"
- **TC_UI_02**: Removed actual result - marked as "Not Run"
- **TC_NAV_01**: Removed actual result - marked as "Not Run"
- **TC_NAV_02**: Removed actual result - marked as "Not Run"

**Rule**: Only record "Actual Result" after genuinely executing the test case.

---

### 2. ✅ Removed Real Payment Card Number

**Issue**: TC_CHECKOUT_03 referenced a payment card number (4242 4242 4242 4242).

**Fix:**
- **Before**: `Card: 4242 4242 4242 4242`
- **After**: `Comment: 'Test order'; Payment details: per site's test payment instructions`
- **Reason**: Never include real payment details in test documentation; test payment flow must be verified with site's documentation first

**Note Added**: "Payment flow requires test card details from site documentation - do not use real payment information"

---

### 3. ✅ Made TC_LOGIN_07 Security Test More Specific

**Issue**: Vague expected result: "Login blocked or error shown"

**Fix:**
- **Expected Result**: More specific but acknowledges multiple valid outcomes
- **Actual Result**: Left empty (Not Run)
- **Status**: Changed to "Not Run"
- **Note**: "Security test - requires manual verification with network inspection"

**Why Not Automated**: Security tests like SQL injection require:
- Network traffic inspection
- Server log analysis  
- Verification that injection string wasn't processed
- Manual security review of server response

---

### 4. ✅ Made Expected Results More Specific

**Issue**: Vague expected results that don't provide clear pass/fail criteria.

#### TC_PROD_05 - View Product Details
**Before**: "Full product details displayed"
**After**: "Product detail page shows: product name; category (e.g. Women > Tops); price; availability status; condition (New); brand name; full description paragraph; product images"

#### TC_PROD_06 - Filter Products by Category
**Before**: "Products filtered by category"
**After**: "Page displays only products matching selected category; heading updates to show category name; product count matches category selection"

#### TC_CART_04 - Update Quantity
**Before**: "Price updated correctly (3x item price)"
**After**: "Total price column updates automatically to show 3 × unit price; cart totals section reflects new quantity in subtotal and total"

#### TC_CART_06 - Add Same Product Multiple Times
**Before**: "2 line items or quantity=2"
**After**: "Cart displays either: (Option A) 1 row with quantity 2 OR (Option B) 2 separate rows for same product"

#### TC_CHECKOUT_03 - Complete Order with Payment
**Before**: "Order confirmation page shown"
**After**: "Order placed successfully; confirmation page shows: 'ORDER PLACED!' or 'Congratulations!' message; order number; download invoice option"

#### TC_UI_01 - Site Logo
**Before**: "Logo visible in header"
**After**: "Header contains: site logo image with alt text 'Website for automation practice'; navigation menu with Home Products Cart links"

#### TC_UI_02 - Footer Links
**Before**: "Footer with subscription and social links"
**After**: "Footer displays: SUBSCRIPTION heading; email input field with placeholder 'Your email address'; arrow submit button; social media icons"

#### TC_NAV_01 - Contact Us Navigation
**Before**: "Contact form displayed"
**After**: "Contact Us page loads showing: 'GET IN TOUCH' heading; name email subject message fields; contact form; upload file option"

#### TC_NAV_02 - Newsletter Subscription
**Before**: "You have been successfully subscribed!"
**After**: "Success alert appears with message 'You have been successfully subscribed!' (alert box)"

---

## Improved Test Cases - Before/After Examples

### Example 1: TC_PROD_05
```diff
- Expected: Full product details displayed
- Actual: Full product details displayed
- Status: Pass

+ Expected: Product detail page shows: product name; category (e.g. Women > Tops); 
+           price; availability status; condition (New); brand name; full 
+           description paragraph; product images
+ Actual: (empty - not executed yet)
+ Status: Not Run
```

### Example 2: TC_CHECKOUT_03
```diff
- Test Data: Card: 4242 4242 4242 4242
- Expected: Order confirmation page shown
- Actual: Order confirmation page shown
- Status: Pass

+ Test Data: Comment: 'Test order'; Payment details: per site's test payment instructions
+ Expected: Order placed successfully; confirmation page shows: 'ORDER PLACED!' or 
+           'Congratulations!' message; order number; download invoice option
+ Actual: (empty - not executed yet)
+ Status: Not Run
+ Notes: Payment flow requires test card details from site documentation - 
+        do not use real payment information
```

### Example 3: TC_LOGIN_07
```diff
- Expected: Login blocked or error shown
- Actual: Login blocked or error shown
- Status: Pass

+ Expected: Login fails with error or SQL injection is prevented
+ Actual: (empty - not executed yet)
+ Status: Not Run
+ Notes: Security test - requires manual verification with network inspection
```

---

## Best Practices Applied

### 1. **Specific Expected Results**
- List exact elements/messages to verify
- Include example values in parentheses
- Specify format (e.g., "Rs. [amount]")
- Name specific UI elements
- State exact text when known

### 2. **Realistic Test Status**
- **Pass**: Only for executed automated tests with actual results
- **Not Run**: For manual tests not yet executed
- Never claim "Pass" without executing the test

### 3. **Security in Test Data**
- Never include real payment card numbers
- Never include real credentials in CSV
- Reference external documentation for sensitive data
- Use placeholder text like "per site's test payment instructions"

### 4. **Clear Automation Rationale**
Each "No" in Automated column has specific reason:
- Security tests require manual verification
- Visual tests better suited for manual review
- Edge cases need investigation before automation
- Features require additional implementation effort

---

## Statistics

### Test Cases: 29 Total
- **Automated (Yes)**: 18 tests (62%)
- **Manual/Not Yet Run**: 11 tests (38%)

### Status Distribution
- **Pass**: 18 (automated tests with actual results)
- **Not Run**: 11 (manual tests awaiting execution)
- **Fail**: 0

### Improvements Made
- ✅ Removed 11 premature "Actual Result" entries
- ✅ Removed 1 real payment card number
- ✅ Improved 10 vague expected results
- ✅ Added specific security test guidance
- ✅ Added notes for 11 manual test cases

---

## Validation

```bash
python check_csv.py
# CSV check passed! 29 test cases checked.
```

All test cases now meet quality standards:
- Specific, measurable expected results
- Appropriate status values
- No premature actual results
- No sensitive data exposure
- Clear automation decisions

---

## Interview-Ready Points

**"How do you write good test cases?"**
- Specific expected results with exact elements/messages
- Only record actual results after execution
- Never include sensitive data (payment cards, real credentials)
- Clear pass/fail criteria
- Realistic status tracking

**"Why are some tests manual?"**
- Security tests need specialized verification (TC_LOGIN_07)
- Visual tests better for human review (TC_UI_01-02)
- Edge cases need investigation first (TC_CART_06)
- Features pending implementation (TC_CART_04)

**"How do you handle payment testing?"**
- Verify site's test payment documentation first
- Never use real payment card numbers
- Reference external test card details
- Validate test environment supports safe payment testing
