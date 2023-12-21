
"""
NOTES
what is the workflow that needs to happen?

log into a device
- I need to know IP address
- I need to know which ios im running

run a dir command
- There is a Genie parser
- capture this data

Gather the ios file i need to be on there for upgrade

compare my file to file on device.
- if file not on device run fail.
- This is okay if this fails on the pre check, the next logical step would be to deploy image.

close connection to the device.






"""
import re
import logging
from ats import aetest
from pprint import pprint
from ats.log.utils import banner
#
# create a logger for this testscript
#
logger = logging.getLogger(__name__)
#
# Common Setup Section
#
class common_setup(aetest.CommonSetup):
    '''Common Setup Section

    Defines subsections that performs configuration common to the entire script.

    '''
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        #testbed.connect(log_stdout=False)
        testbed.connect(log_stdout=False)
        
    @aetest.subsection
    def loop_mark(self, testbed):
        # this is to loop over your devices in testbed for the tests you want to run.
        aetest.loop.mark(deviceUpgradePreCheck, device_name=testbed.devices)

class deviceUpgradePreCheck(aetest.Testcase):
    
    @aetest.test
    def setup(self, testbed, device_name):
        """ Testcase Setup section """
        # connect to device
        self.device = testbed.devices[device_name]

    @aetest.test
    def bin_file_on_device(self):
        CISCO_IOS_FILE = "vios-adventerprisek9--m" # Failing test
        #CISCO_IOS_FILE = "vios-adventerprisek9-m" # Working test
        dir_response = self.device.parse("dir")
        for key, value in dir_response.items():
            value_2 = value["flash0:/"]["files"]
            if CISCO_IOS_FILE not in value_2:
                self.failed(f"OS - {CISCO_IOS_FILE} is not on {self.device.name}")
    
    @aetest.test
    def cdp_neighbors_on_device(self):
        cdp_neighbors = self.device.parse("show cdp neighbors")
            
    @aetest.test
    def free_space_on_device(self):
        CISCO_FILE_SIZE = 198767002
        dir_response = self.device.parse("dir")
        free_space = dir_response["dir"]["flash0:/"]["bytes_free"]
        if int(free_space) < CISCO_FILE_SIZE :
            self.failed(f"fail")

# ----------------
# AE Test Cleanup
# ----------------
class common_cleanup(aetest.CommonCleanup):
    """Common Setup section"""
# ----------------
# Connected to devices
# ----------------
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        """Connect to all the devices"""
        testbed.disconnect()


# for running as its own executable
if __name__ == '__main__':

    # local imports
    import argparse
    from ats.topology import loader
    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--ios', dest = 'ios_names', type = list, default = ['router10','router17'])
    parser.add_argument('--testbed', dest = 'testbed', type = loader.load, default = '/home/angella/git/github/NetDevOps/Testing/pyATS/my_testbed.yaml')
    # parse args
    args, unknown = parser.parse_known_args()
    #and pass all arguments to aetest.main() as kwargs
    aetest.main(**vars(args))
