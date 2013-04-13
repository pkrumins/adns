from slow_dns import resolve_slow
import sys
from time import time
hosts=list(sys.argv)
hosts.pop(0)

start = time()
resolved = resolve_slow(hosts)
end = time()

print "-------------------------------------------"
for host, ip in resolved.items():
  if ip is None:
        	print "--%s could not be resolved." % host
      	else:
        	print "--%s resolved to %s" % (host, ip)
print "-------------------------------------------"
print "It took %.2f seconds to resolve %d hosts." % (end-start, len(sys.argv)-1)
print "-------------------------------------------"
