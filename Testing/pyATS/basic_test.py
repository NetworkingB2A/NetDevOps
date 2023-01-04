from genie.testbed import load
testbed = load('working-tb.yaml')
device = testbed.devices['nx-osv-1']
device.connect()
output = device.execute('show version')
print(output)
'7.3' in output
if '7.3' in output:
    print("'7.3' was found in the output!")
parsed = device.parse('show version')
parsed
from pprint import pprint
pprint(parsed)
parsed2 = device.parse('show vrf')

pprint(parsed2)

parsed2['vrfs']['default']['vrf_id']
parsed2['vrfs']['default']['vrf_state']

for vrf in parsed2['vrfs']:
    vrf_id = parsed2['vrfs'][vrf]['vrf_id']
    vrf_state = parsed2['vrfs'][vrf]['vrf_state']
    print('Vrf {vrf} is {state}'.format(vrf=vrf_id, state=vrf_state))
configuration = '''\
interface ethernet2/1
shutdown'''

output = device.configure(configuration)
configuration = [
    'interface ethernet2/1',
    'shutdown'
]

output = device.configure(configuration)
output = device.learn('interface')
pprint(output.info)