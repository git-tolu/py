# # import mccormerce.shipping
# # from mccormerce.shipping  import calc_shipping
# from mccormerce  import shipping
# # mccormerce.shipping.calc_shipping()
# # calc_shipping()
# shipping.calc_shipping()

from pathlib import Path

path = Path("")
# path = Path("ut")
# print(path.rmdir())
# print(path.glob("*.py"))

for file in path.glob("*"):
  print(file)



