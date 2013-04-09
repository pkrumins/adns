from async_dns import AsyncResolver
ar = AsyncResolver(
           ["www.google.com", "www.reddit.com", "www.nonexistz.net"]
    )
resolved = ar.resolve()

for host, ip in resolved.items():
  if ip is None:
        	print "%s could not be resolved." % host
      	else:
        	print "%s resolved to %s" % (host, ip)
