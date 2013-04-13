from async_dns import AsyncResolver
import sys
ar = AsyncResolver(
           list(sys.argv)
    )
resolved = ar.resolve()

for host, ip in resolved.items():
  if ip is None:
        	print "%s could not be resolved." % host
      	else:
        	print "%s resolved to %s" % (host, ip)
