#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# Asynchronous DNS Resolution. v1.0.
#
# Read more about this code at:
# http://www.catonmat.net/blog/asynchronous-dns-resolution
#

import adns
from time import time
import sys

class AsyncResolver(object):
    def __init__(self, hosts, intensity=100):
        """
        hosts: a list of hosts to resolve
        intensity: how many hosts to resolve at once
        """
        self.hosts = hosts
        self.intensity = intensity
        self.adns = adns.init()

    def resolve(self):
        """ Resolves hosts and returns a dictionary of { 'host': 'ip' }. """
        resolved_hosts = {}
        active_queries = {}
        host_queue = self.hosts[:]

        def collect_results():
            for query in self.adns.completed():
                answer = query.check()
                host = active_queries[query]
                del active_queries[query]
                if answer[0] == 0:
                    ip = answer[3][0]
                    resolved_hosts[host] = ip
                elif answer[0] == 101: # CNAME
                    query = self.adns.submit(answer[1], adns.rr.A)
                    active_queries[query] = host
                else:
                    resolved_hosts[host] = None

        def finished_resolving():
            return len(resolved_hosts) == len(self.hosts)

        while not finished_resolving():
            while host_queue and len(active_queries) < self.intensity:
                host = host_queue.pop()
                query = self.adns.submit(host, adns.rr.A)
                active_queries[query] = host
            collect_results()

        return resolved_hosts


if __name__ == "__main__":
    write_mode = 'a' #append
    
    if len(sys.argv) != 3:
        print 'Usage:', sys.argv[0], "input.txt output.txt"
        exit()
                
    in_file = sys.argv[1]
    out_file = sys.argv[2]    
    
    # read hosts from input file 
    with open(in_file, 'r') as f:
        hosts = [line.strip() for line in f.readlines()]    
    
    ar = AsyncResolver(hosts, intensity=500)
    start = time()    
    resolved_hosts = ar.resolve()
    end = time()    
    
    print "It took %.2f seconds to resolve %d hosts." % (end-start, len(hosts))
    
    # write results to output file
    with open(out_file, write_mode) as f:
        for key, item in resolved_hosts.items():
            if item is None:
                f.write("%s could not be resolved\n" % key)
            else:
                f.write("%s resolved to %s\n" %(key, item))
