# -*- coding: utf-8 -*-
"""Compatibilidade com Termux/Android."""
import os

def fix_dns():
    """Faz o dnspython funcionar sem /etc/resolv.conf."""
    try:
        import dns.resolver
    except ImportError:
        return
    if getattr(dns.resolver, '_termux_patched', False):
        return
    _Original = dns.resolver.Resolver
    class TermuxResolver(_Original):
        def __init__(self, *args, **kwargs):
            try:
                _Original.__init__(self, *args, **kwargs)
            except Exception:
                _Original.__init__(self, configure=False)
                self.nameservers = ['8.8.8.8', '1.1.1.1']
    dns.resolver.Resolver = TermuxResolver
    dns.resolver._termux_patched = True

def dns_query(domain, rtype='A'):
    fix_dns()
    import dns.resolver
    if hasattr(dns.resolver, 'resolve'):
        return dns.resolver.resolve(domain, rtype)
    return dns.resolver.query(domain, rtype)

fix_dns()
