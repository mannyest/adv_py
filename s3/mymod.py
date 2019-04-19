# sample module

REPODIR = '/path/to/commonly/used/directory'

SERVER_LIST = [ 'dataserv.company.com', 
                'personnel.company.com', 
                'stats.company.com'      ]

def addthese(arg1, arg2):
    # function raises TypeError if objects 
    # are not of correct type
    if ( not isinstance(arg1, (int, float)) or 
         not isinstance(arg2, (int, float))    ):
        raise TypeError('both args must be numeric type')

    argsum = arg1 + arg2
    return argsum


