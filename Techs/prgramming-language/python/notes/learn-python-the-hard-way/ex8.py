formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

formatter_r = "%r %r %r %r"
formatter_s = "%s %s %s %s"
print formatter_s % (formatter_s, formatter_s, formatter_s, formatter_s)
print formatter_s % (formatter_r, formatter_r, formatter_r, formatter_r)

print formatter_r % (formatter_r, formatter_r, formatter_r, formatter_r)
print formatter_r % (formatter_s, formatter_s, formatter_s, formatter_s)

print formatter_s % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
