from async_dns import AsyncResolver
import sys
from time import time
hosts=list(sys.argv)
hosts.pop(0)
ar = AsyncResolver(
           hosts
    )
start = time()
resolved = ar.resolve()
end = time()

print "-------------------------------------------"
for host, ip in resolved.items():
  if ip is None:
        	print "%s could not be resolved." % host
      	else:
        	print "%s resolved to %s" % (host, ip)
print "-------------------------------------------"
print "It took %.2f seconds to resolve %d hosts." % (end-start, len(sys.argv)-1)
print "-------------------------------------------"
