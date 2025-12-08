local elf = require("utils.helper")
local grid = {}
local start_r = 1
local start_c = 1

for line in io.lines("puzzle.txt") do
    table.insert(grid, line)
end

for i = 1, #grid[1] do
    if elf.char_at(grid[1], i) == "S" then
        start_c = i
        break
    end
end

local cache = {}
local unique_splitters = {}

local function beam(row, col)
    local key = row .. "," .. col
    if cache[key] then
        return cache[key]
    end

    if row > #grid then
        return 1
    end

    local char = elf.char_at(grid[row], col)
    if char == nil then
        return 1
    end

    local path_count
    if char == "^" then
        if not unique_splitters[key] then
            unique_splitters[key] = true
        end

        path_count = beam(row + 1, col - 1) + beam(row + 1, col + 1)
    else
        path_count = beam(row + 1, col)
    end

    cache[key] = path_count
    return path_count
end

local part2_result = beam(start_r, start_c)
local part1_count = 0
for _ in pairs(unique_splitters) do
    part1_count = part1_count + 1
end

print("Part 1:", part1_count)
print("Part 2:", part2_result)
