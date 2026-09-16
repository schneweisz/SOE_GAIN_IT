import utils.math_utils as mu # teljes package hívása aliassal
#import utils.string_utils #érdemes aliast adni, mert különben útvonalt is írni kell
import utils.string_utils as string_utils
from utils.number_utils import is_even # egy fg hívása 

print(mu.add(2, 3))
#print(utils.string_utils.shout("hello"))
print(string_utils.shout("hello"))
print(is_even(4))
