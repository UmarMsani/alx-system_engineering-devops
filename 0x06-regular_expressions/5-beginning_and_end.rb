#!/usr/bin/env ruby

# Accept the argument and pass it to the regular expression matching method
puts ARGV[0].scan(/^h.n$/).join
