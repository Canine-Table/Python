#!/usr/bin/python3

_h = "hello world"
_i = "hello world"
_none = None
_not_imp = NotImplemented
_ellipsis = Ellipsis
_float = 3.14195
_int = 314195
_bool = 0


print("memory location of h:",id(_h))
print("h is of type:",type(_h))
print("the truth value of _h is _i:",_h is _i)

print("truth, value",_none,"is:",bool(_none))
print("the truth value of",_ellipsis,"is:",bool(_ellipsis))
print("value of not_imp is:",_not_imp)

