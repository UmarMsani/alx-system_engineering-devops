#!/usr/bin/env ruby

# Read the log file content
log_content = ARGF.read

# Extract sender, receiver, and flags
sender = log_content[/from:([^\]]+)/, 1]
receiver = log_content[/to:([^\]]+)/, 1]
flags = log_content[/flags:([^\]]+)/, 1]

# Print the formatted output
puts "#{sender},#{receiver},#{flags}"
