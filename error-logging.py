'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

import sys
import logging

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)
                        
try: a+b

except Exception as e:
    logging.error(error_handling())