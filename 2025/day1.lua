MIN = 0
MAX = 99
RANGE = MAX - MIN + 1

local function part1()
  local value = 50
  local password = 0

  for line in io.lines("puzzle.txt") do
    local step = line:sub(2)

    if line:match("^L") then
      value = value - step
    elseif line:match("^R") then
      value = value + step
    end

    value = (value % RANGE + RANGE) % RANGE
    if value == 0 then
      password = password + 1
    end
  end

  return password
end

local function count_zeros(value, step)
  local zeros = math.floor(math.abs(step) / RANGE)
  local remainder = math.abs(step) % RANGE
  local distance_to_zero

  if step > 0 then
    distance_to_zero = (RANGE - value) % RANGE
    if distance_to_zero == 0 then
      distance_to_zero = RANGE
    end

    if distance_to_zero <= remainder then
      zeros = zeros + 1
    end
  else
    distance_to_zero = value
    if distance_to_zero == 0 then
      distance_to_zero = RANGE
    end

    if distance_to_zero <= remainder then
      zeros = zeros + 1
    end
  end

  return zeros
end

local function part2()
  local value = 50
  local password = 0

  -- print("value", "line", "password")
  for line in io.lines("puzzle.txt") do
    local step = tonumber(line:sub(2))

    if line:match("^L") then
      password = password + count_zeros(value, -step)
      -- print(value, line, password)
      value = value - step
    elseif line:match("^R") then
      password = password + count_zeros(value, step)
      -- print(value, line, password)
      value = value + step
    end

    value = (value % RANGE + RANGE) % RANGE
  end
  -- print(value, "---", "-")

  return password
end

local part1_result = part1()
print("Part 1:", part1_result)

local part2_result = part2()
print("Part 2:", part2_result)
