#!/usr/bin/python

import urllib2
import re

response = urllib2.urlopen('https://www.spamhaus.org/drop/drop.txt')
lines = response.read().split("\n")

# lines prefixed by ';' go into header
header = [line for line in lines if line.startswith(';')]

# parse ip blocks and id's}
tuples = [line.split(';') for line in lines if not line.startswith(';')]

for i in range(len(tuples)-1):
  #print "tuples[" + str(i) + "][0]=" + tuples[i][0], "; tuples[" + str(i) + "][1]=", tuples[i][1]
  print "'Spamhaus {}':      source => '{}', jump => \"DROP\";'".format(tuples[i][1].strip(), tuples[i][0].strip())

"""
; Spamhaus DROP List 2016/08/16 - (c) 2016 The Spamhaus Project
; https://www.spamhaus.org/drop/drop.txt
; Last-Modified: Tue, 16 Aug 2016 08:33:46 GMT
; Expires: Tue, 16 Aug 2016 16:01:19 GMT
1.4.0.0/17 ; SBL256893
1.10.16.0/20 ; SBL256894
"""


"""
# == Class: iptables::haproxy_drop
#
# This class drops Spamers from hitting the haproxy frontends.
#
# === Parameters
#
# === Actions
#
# - Blocks bad IP blocks to Fronend HAProxy Servers.
#
# === Requires
#
# === Sample Usage
#
#   class { 'iptables::haproxy_drop': }
#
class iptables::haproxy_drop {

  iptables {
      'Bad SPAM IP - Flow ID: Block 3-22-2016':      source => '185.143.241.59/32', jump => "DROP";
      'Bad SPAM IP 2999 - Flow ID: Block 8-17-2016': source => '62.69.45.11', jump => "DROP";
  }
}
"""

	
