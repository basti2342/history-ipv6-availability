#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, sqlite3, socket
from os import path
from datetime import datetime

if not (len(sys.argv) > 1 and path.isfile(sys.argv[1])):
	print "Please call this script with your Firefox's places.sqlite."
	quit()

# define period
start = datetime(2014, 1, 1)
end = datetime(2015, 1, 1)

db = sqlite3.connect(sys.argv[1])
c = db.cursor()

c.execute("SELECT rev_host, visit_count FROM moz_places WHERE last_visit_date" \
	+ " BETWEEN %d AND %d GROUP BY rev_host ORDER BY visit_count DESC" \
	% (time.mktime(start.timetuple()) * 1e6, time.mktime(end.timetuple()) * 1e6))

v6available = {True: 0, False: 0}
for row in c:
	host, count = row
	host = host[-2::-1]
	try:
		addresses = [result[4][0] for result in socket.getaddrinfo(host, 80)]
		v6 = True if ":" in "".join(addresses) else False
	except socket.gaierror:
		print host, "unresolvable"
		continue
	print host, v6
	v6available[v6] += 1

numHosts = sum(v6available.values())
percentageReady = v6available[True]*100/float(numHosts)
print "%d out of %d hosts are IPv6 ready (%.2f%%)." \
	% (v6available[True], numHosts, percentageReady)
