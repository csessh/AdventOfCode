M = {}

function M.load_puzzle_input()
  local file = io.open("puzzle.txt", "r")
  if file ~= nil then
    local content = file:read("*a")
    file:close()
    return content
  end
end

return M
