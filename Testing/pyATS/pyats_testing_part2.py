











import re
import logging
from ats import aetest
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
        testbed.connect(log_stdout=False)
        
    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Enable_CDP, device_name=testbed.devices)
        aetest.loop.mark(PING_Public_IPs, device_name=testbed.devices)

class Enable_CDP(aetest.Testcase):
    """Enable CDP On all Devices and Physical Interfaces"""

    @aetest.test
    def setup(self, testbed, device_name):
        """ Testcase Setup section """
        # connect to device
        self.device = testbed.devices[device_name]
        # Loop over devices in tested for testing


    @aetest.test
    def enable_CDP_interfaces(self):
        interfaces = self.device.parse("show ip interface brief")
        for interface in interfaces['interface'].items():
            if self.device.os == "iosxe":
                if "Gigabit" in interface:
                    self.device.configure(f""" interface { interface }
                    cdp enable
                    """)
            elif self.device.os == "nxos":
                if "Ethernet" in interface:
                    self.device.configure(f""" interface { interface }
                    cdp enable
                    """)
        time.sleep(15)
    








class common_cleanup(aetest.CommonCleanup):
    '''disconnect from ios routers'''

    @aetest.subsection
    def disconnect(self, steps, ios_names):
        '''disconnect from both devices'''
        for ios_name in ios_names:
            with steps.start('Disconnecting from ios device: %s'%(ios_name)):
                self.parameters[ios_name]['ios'].disconnect()
            if self.parameters[ios_name]['ios'].connected:
                # abort/fail the testscript if device connection still exists
                self.failed('One of the devices could not be disconnected from',
                        goto = ['exit'])

if __name__ == '__main__':

    # local imports
    import argparse
    from ats.topology import loader
    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--ios', dest = 'ios_names', type = list, default = ['router10','router17'])
    parser.add_argument('--testbed', dest = 'testbed', type = loader.load, default = 'my_testbed.yaml')
    # parse args
    args, unknown = parser.parse_known_args()
    #and pass all arguments to aetest.main() as kwargs
    aetest.main(**vars(args))
