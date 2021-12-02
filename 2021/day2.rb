instructions = Array.new

File.open('test.txt', 'r') do |f|
    f.each_line do |line|
        instructions.push(line)
    end
end

# Part 1
x = y = 0
instructions.each do |instruction|
    dir, val = instruction.split
    val = val.to_i
    if dir == 'forward'
        x += val
    elsif dir == 'down'
        y += val
    elsif dir == 'up'
        y -= val
    end
end
puts x*y

# Part 2
x = y = aim = 0
instructions.each do |instruction|
    dir, val = instruction.split
    val = val.to_i
    if dir == 'forward'
        x += val
        y += aim * val
    elsif dir == 'down'
        aim += val
    elsif dir == 'up'
        aim -= val
    end
end
puts x*y