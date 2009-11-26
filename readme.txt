This is a tiny Python library for resolving a lot of DNS records
asynchronously. On a speedy internet connection it managed to do
20,000 resolutions per minute.

It was written by Peteris Krumins (peter@catonmat.net).
His blog is at http://www.catonmat.net  --  good coders code, great reuse.

The code is licensed under the MIT license.

The code was written as a part of the article "Resolving DNS Asynchronously"
on my website. The whole article can be read at:

    http://www.catonmat.net/blog/asynchronous-dns-resolution/

------------------------------------------------------------------------------

Table of contents:
    [1] The problem.
    [2] The solution and how to use async_dns.py
    [3] What is slow_dns.py included in this source tree?


[1]-The-problem---------------------------------------------------------------

Once upon a time, I had to quickly resolve thousands of DNS names. My first
solution was to call gethostbyname repeatedly for each of the hosts. This
turned out to be extremely slow. I could only do 200 hosts in a minute. I
talked with someone and he suggested to try to do it asynchronously. I looked
around and found adns - asynchronous dns library written in C (see link (1)
below). Since I was writing the code in Python, I looked around some more and
found Python bindings for adns (see link (2) below). I tried adns and - wow -
I could do 20,000 hosts in a minute!

...

Continue reading on http://www.catonmat.net/blog/asynchronous-dns-resolution/

Link references:

    (1) http://www.chiark.greenend.org.uk/~ian/adns/
    (2) http://code.google.com/p/adns-python/

[2]-The-solution--------------------------------------------------------------

I wrote async_dns.py Python module to do the resolution. It uses Python
wrapper for adns C library (see links (1) and (2) above).

The async_dns.py module exports AsyncResolver class. The constructor of this
class takes a list of domains to resolve.

Here is an example that resolves three domains asynchronously:

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

The constructor of Asynchronously also takes 'intensity' paramter, which
specifies how many hosts to resolve asynchronously at once.

Calling the resolve() member function on an AsyncResolver object starts
resolving all the domains that were passed to AsyncResolver constructor.

Once it's done, it returns a dictionary of { 'host': 'ip' } structure.

[3]-What-is-slow_dns.py-in-the-source-tree?-----------------------------------

The file slow_dns.py is my first attempt at resolving a lot of DNS hosts. It
uses the standard system resolver "gethostbyname" from Python's socket module.

It can only do 200 resolutions per minute.

Python module slow_dns.py exports resolve_slow function, it takes a list of
hosts as an argument, resolves them, and returns a dictionary of
{ 'host': 'ip' } pairs.

You can use it the following way:

    from slow_dns import resolve_slow

    resolved = resolve_slow(['www.reddit.com', 'www.catonmat.net'])
    for host, ip in resolved.items():
      if ip is None:
        print "%s could not be resolved." % host
      else:
        print "%s resolved to %s" % (host, ip)


------------------------------------------------------------------------------

See my original article for more information on both async_dns.py and
slow_dns.py.

It's here:

    http://www.catonmat.net/blog/asynchronous-dns-resolution/

------------------------------------------------------------------------------

That's it. Happy asynchronous resolution!


Sincerely,
Peteris Krumins
http://www.catonmat.net

