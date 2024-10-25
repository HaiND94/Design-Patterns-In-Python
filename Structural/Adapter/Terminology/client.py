from a import A
from b import B
from adapter import ClassBAdapter

ITEMS = [A(), B()]

for item in ITEMS:
    if isinstance(item, B):
        item.method_b()
        continue
    item.method_a()