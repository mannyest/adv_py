##importing module cProfile and also importing a script in same directory (test.py)
##then running cProfile.run(.main())

import test
import cProfile

cProfile.run('test.main()')
