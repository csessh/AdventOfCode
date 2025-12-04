local elf = require("utils.helper")

local function is_invalid_two_part_pattern(n)
  local t = tostring(n)
  if #t % 2 ~= 0 then
    return false
  end

  local mid = #t / 2
  local left = string.sub(t, 1, mid)
  local right = string.sub(t, mid + 1)
  return left == right
end

-- KMP algorithm to find substring periodicity
local function kmp(s)
  local fail = {}
  for i = 1, #s do
    fail[i] = 0
  end

  for i = 2, #s do
    local j = fail[i - 1]
    while j > 0 and s:byte(i) ~= s:byte(j + 1) do
      j = fail[j]
    end

    if s:byte(i) == s:byte(j + 1) then
      j = j + 1
    end

    fail[i] = j
  end

  local period_len = #s - fail[#s]
  if #s % period_len == 0 then
    return s:sub(1, period_len)
  end

  return s
end

local function main()
  local part1 = 0
  local part2 = 0
  local content

  local file = io.open("puzzle.txt", "r")
  if file ~= nil then
    content = file:read("*a")
    file:close()
  end

  local ranges = elf.split(content, ",")
  for _, v in ipairs(ranges) do
    local start_id
    local end_id

    local range = elf.split(v, "-")
    start_id = tonumber(range[1])
    end_id = tonumber(range[2])

    for n = start_id, end_id do
      if is_invalid_two_part_pattern(n) then
        part1 = part1 + n
      end

      if kmp(tostring(n)) ~= tostring(n) then
        part2 = part2 + n
      end
    end
  end

  print("Part 1: ", part1)
  print("Part 2: ", part2)
end

assert(is_invalid_two_part_pattern("1") == false, "1 should be a valid id")
assert(is_invalid_two_part_pattern("101") == false, "101 should be a valid id")
assert(is_invalid_two_part_pattern("1188511886") == false, "1188511886 should be a valid id")
assert(is_invalid_two_part_pattern("222") == false, "222 should be a valid id")
assert(is_invalid_two_part_pattern("11") == true, "11 should be an invalid id")
assert(is_invalid_two_part_pattern("2222") == true, "2222 should be an invalid id")
assert(is_invalid_two_part_pattern("1188511885") == true, "1188511885 should be an invalid id")
assert(kmp("123123") == "123")
assert(kmp("111") == "1")
assert(kmp("1111") == "1")
assert(kmp("21212121") == "21")
assert(kmp("212121214") == "212121214")
assert(kmp("123") == "123")
assert(kmp("313") == "313")

main()
