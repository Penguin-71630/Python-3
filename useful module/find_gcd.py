# how to use : gcd_of_n_list(0, 1, a_list_of_number)
# return : GCD of given list of numbers


def gcd_of_n_list(a, b, given_list):
    n_list = given_list

    if b < len(n_list):
        q = n_list[b]
        p = n_list[a] if a == 0 else a

        while p != 0 and q != 0:
            p, q = q, p % q

        return gcd_of_n_list(p + q, b + 1, n_list)
    else:
        return a
