local elf = require("utils.helper")

local function part1()
    local digits = {}
    for line in io.lines("puzzle.txt") do
        local splits = elf.split(line, " ")
        table.insert(digits, splits)
    end

    local ops = digits[#digits]
    local result = 0

    for i = 1, #ops do
        local tmp = 0
        for j = 1, #digits - 1 do
            if ops[i] == "+" then
                tmp = tmp + digits[j][i]
            elseif ops[i] == "*" then
                if tmp == 0 then
                    tmp = 1
                end
                tmp = tmp * digits[j][i]
            end
        end

        result = result + tmp
    end

    print("Part 1:", result)
end

local function part2()
    local digits = {}

    for line in io.lines("puzzle.txt") do
        table.insert(digits, line)
    end

    local result = 0
    local buffer = {}

    for c = #digits[1], 1, -1 do
        local n = ""
        for i = 1, #digits - 1 do
            n = n .. elf.char_at(digits[i], c)
        end

        if tonumber(n) ~= nil then
            table.insert(buffer, tonumber(n))
        end

        local op = elf.char_at(digits[#digits], c)
        if op == "*" then
            result = result + elf.product(buffer)
            buffer = {}
        elseif op == "+" then
            result = result + elf.sum(buffer)
            buffer = {}
        end
    end

    print("Part 2:", result)
end

part1()
part2()
