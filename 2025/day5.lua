local elf = require("utils.helper")

local ranges = {}
local ingredients = {}

local function parse_input()
    local is_parsing_ranges = true
    for line in io.lines("puzzle.txt") do
        if line == "" then
            is_parsing_ranges = false
        else
            if is_parsing_ranges then
                local range = elf.split(line, "-")
                table.insert(ranges, { tonumber(range[1]), tonumber(range[2]) })
            else
                table.insert(ingredients, tonumber(line))
            end
        end
    end
end

local function validate()
    local count = 0
    for _, i in ipairs(ingredients) do
        for _, r in ipairs(ranges) do
            if i >= r[1] and i <= r[2] then
                count = count + 1
                break
            end

            if i < r[1] then
                break
            end
        end
    end

    print("Part 1:", count)
end

local function transform()
    table.sort(ranges, function(a, b)
        return a[1] < b[1]
    end)

    local merged = {}
    for _, r in ipairs(ranges) do
        if #merged == 0 or r[1] > merged[#merged][2] + 1 then
            -- No overlap, add new range
            table.insert(merged, { r[1], r[2] })
        else
            -- Overlap, extend current range
            merged[#merged][2] = math.max(merged[#merged][2], r[2])
        end
    end
    ranges = merged

    local count = 0
    for _, r in ipairs(ranges) do
        count = count + (r[2] - r[1] + 1)
    end

    print("Part 2:", count)
end

parse_input()
transform()
validate()
