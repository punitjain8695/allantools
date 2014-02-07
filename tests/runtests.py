

# this files runs all the tests defined in the subdirectories

import time
import sys
sys.path.append("..") # allows importing allantools from parent dir


from nbs14 import nbs14_test
from phasedat import phase_dat_test
from pink_frequency import pink
from Cs5071A import Cs5071A_test_decade

if __name__ == "__main__":
	
	start = time.clock()
	
	nbs14_test.run()          # NBS14 test data with published deviations
	phase_dat_test.run()      # phase.dat from Stable32
	pink.run()                # synthetic pink frequency noise
	Cs5071A_test_decade.run() # HP 5071A Cs-clock measured against H-maser
	
	end = time.clock()
	print "Tests done in %2.3f s" % (end-start) # ca 58 seconds on an i7 CPU
