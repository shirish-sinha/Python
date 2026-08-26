# Task 9 - Floor Division Edge Cases
# Test floor division with all sign combinations.

positive1 = 20
positive2 = 3
negative1 = -20
negative2 = -3

print("positive // positive:", positive1, "//", positive2, "=", positive1 // positive2)
print("negative // positive:", negative1, "//", positive2, "=", negative1 // positive2)
print("positive // negative:", positive1, "//", negative2, "=", positive1 // negative2)
print("negative // negative:", negative1, "//", negative2, "=", negative1 // negative2)

# Explanation:
# Floor division always rounds DOWN toward negative infinity, not toward zero.
# For example, -20 // 3 = -6.666... and flooring it means rounding down to -7,
# not truncating to -6. This is why the negative results differ from simply
# removing the decimal part (truncation), which is what languages like C do.
# Python's floor division is consistent: it always picks the largest integer
# that is less than or equal to the true mathematical result.
