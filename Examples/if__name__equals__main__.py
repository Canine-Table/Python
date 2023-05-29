#!/usr/bin/python3

# ******************************* #
#                                 #
#   if __name__ == '__main__':    #
#                                 #
# ******************************* #

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other programs

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# Python will assign the __name__ variable of '__main__' if
# its the initial module being run

import module_one as m_1
if __name__ == '__main__':
    pass

print(__name__)
m_1.hello('Canine Table')
m_1.bye('Canine Table')
m_1.get_name()