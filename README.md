### A Sample Target HTTP Server

This project is meant to assist in development of the Boucan Bug Bounty Canary Platform.

### What is it?

It's a simple flask server that is vulnerable to HTTPoxy. By submitting a "Proxy" header to certain routes, the request will be sent to the proxy (i.e something like Boucan)
