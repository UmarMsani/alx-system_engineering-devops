#!/usr/bin/env ruby

# Accept the argument and check if it's a 10-digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
