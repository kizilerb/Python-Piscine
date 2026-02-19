from load_image import ft_load
from pimp_image import *

#burada yine bir sıkıntı var array biçiminde doğal imagein RGB arrayleri verilmiyor.
array = ft_load("landscape.jpeg")
print(type(array))
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)