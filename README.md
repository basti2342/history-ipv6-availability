# history-ipv6-availability
Checks the hostnames in your Firefox/Iceweasel history for IPv6 availability

This script will check each hostname you visited in 2014 (or what's left of it depending on your history cleaning habits) for AAAA resource records. It won't check if the service is really bound to the IPv6 address.

Usage
-----
Call the script with your Firefox `places.sqlite`:

`python ipv6.py ~/.mozilla/firefox/<profile>.default/places.sqlite`

Result
------
You'll see all hostnames with their result (True means IPv6 ready, False means IPv4 only) or a message that the hostname could not be resolved.
Finally you get the results, e.g.:

`938 out of 5126 hosts are IPv6 ready (18.29%).`

Links
-----
Read the [corresponding blog post](http://randomprojects.de/blog/my-personal-ipv6-report-for-2014/) for further details.
