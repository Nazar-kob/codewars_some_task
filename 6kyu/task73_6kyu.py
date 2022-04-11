# Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster.
# First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on.
# Whenever she names a number, she thinks about all of the digits in that number.
# She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9)
# she has seen at least once so far as part of any number she has named.
# Once she has seen each of the ten digits at least once, she will fall asleep.
# Bleatrix must start with N and must always name (i + 1) × N directly after i × N.
# For example, suppose that Bleatrix picks N = 1692. She would count as follows:
# N = 1692. Now she has seen the digits 1, 2, 6, and 9.
# 2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
# 3N = 5076. Now she has seen all ten digits, and falls asleep.
# The purpose of this kata is to return the last number Bleatrix Trotter sees before falling asleep.
# Input
# Will always be positive integer or zero
# Output
# The last number Bleatrix Trotter sees or "INSOMNIA" (-1 in Rust, C++ and COBOL)
# if she will count forever


def trotter(n):
    some = None
    s = set(str(i) for i in range(10))

    ns = set(str(n))
    count = 2

    while ns != s:
        some = n * count
        ns.update(set(str(some)))
        count += 1
        if some == 0:
            return "INSOMNIA"

    return some
