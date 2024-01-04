#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=to:)\+?\d{11}|(?<=from:)\+?[a-zA-Z0-9]+|(?<=flags:)-?\d+:-?\d+:-?\d+:-?\d+:-?\d+/).join(",")
