# Python3 ,By :- Nikhil_kumar
# Que. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=address.split(".")
        k="[.]".join(l)
        return k

