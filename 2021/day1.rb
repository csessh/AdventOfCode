readings = Array.new

File.open('test.txt', 'r') do |f|
    f.each_line do |line|
        readings.push(line.to_i)
    end
end

#
# Part 1: Single measurement
#
prev = 0
count = -1
readings.each do |reading|
    if reading > prev
        count += 1
    end
    prev = reading
end

puts count

#
# Part 2: Sliding window of three
#
prev = 0
count = -1
readings.each_with_index do |reading, idx|
    measurement = readings[idx, 3].sum()
    if measurement > prev
        count += 1
    end
    prev = measurement
end

puts count