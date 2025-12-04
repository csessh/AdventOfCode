M = {}

function M.load_puzzle_input()
    local file = io.open("puzzle.txt", "r")
    if file ~= nil then
        local content = file:read("*a")
        file:close()
        return content
    end
end

function M.split(str, c)
    if str == nil then
        error("The string is nil, dummy")
    end

    if c == nil then
        error("The separator character is nil, dummy")
    end

    local result = {}
    for word in string.gmatch(str, "([^" .. c .. "]+)") do
        table.insert(result, word)
    end
    return result
end

function M.char_at(s, i)
    return s:sub(i, i)
end

function M.replace_at(s, i, c)
    return s:sub(1, i - 1) .. c .. s:sub(i + 1)
end

function M.display_grid(grid)
    for r = 1, #grid do
        local line = grid[r]
        print(line)
    end
end

return M
