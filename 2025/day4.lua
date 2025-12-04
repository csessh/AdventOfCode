local elf = require("utils.helper")
local grid = {}
local staging = {}
local DIR = {
  -- row, col
  { -1, 0 }, -- Top
  { 1, 0 }, -- Bottom
  { 0, -1 }, -- Left
  { 0, 1 }, -- Right
  { -1, -1 }, -- Top Left
  { -1, 1 }, -- Top Right
  { 1, -1 }, -- Bottom Left
  { 1, 1 }, -- Bottom Right
}

local function is_accessible_by_fork_lift(r, c)
  local count = 0

  for _, dir in ipairs(DIR) do
    local nr = r + dir[1]
    local nc = c + dir[2]

    if nr >= 1 and nr <= #grid and nc >= 1 and nc <= #grid[1] then
      if elf.char_at(grid[nr], nc) == "@" then
        count = count + 1
      end
    end
  end
  return count < 4
end

local function transform()
  local result = 0

  for r = 1, #grid do
    local line = grid[r]
    for c = 1, #line do
      if is_accessible_by_fork_lift(r, c) and elf.char_at(grid[r], c) == "@" then
        result = result + 1
        staging[r] = elf.replace_at(staging[r], c, ".")
      end
    end
  end

  -- Commit
  grid = staging

  os.execute("sleep 0.5")
  -- io.write("\27[2J\27[H")
  -- io.flush()

  elf.display_grid(staging)
  return result
end

local function main()
  for line in io.lines("puzzle.txt") do
    table.insert(grid, line)
    table.insert(staging, line)
  end

  local result = transform()
  print("Part 1:", result)

  local temp = result
  while temp ~= 0 do
    temp = transform()
    result = result + temp
  end

  print("Part 2:", result)
end

main()
