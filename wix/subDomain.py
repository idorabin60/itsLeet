from typing import List
def solve_forall(domains: List[str]):
    result = []
    for domain in domains:
        for dom_res in solve_for_one_domain(domain):
            result.append(dom_res)
    return result


def solve_for_one_domain(cpdomain):
    result = []
    number, domain = cpdomain.split()
    parts = domain.split(".")

    for i in range(len(parts)):
        subdomain = ".".join(parts[i:])
        result.append(f"{number}.{subdomain}")

    return result
cpdomains = ["9001 discuss.leetcode.com"]
print(solve_forall(cpdomains))
