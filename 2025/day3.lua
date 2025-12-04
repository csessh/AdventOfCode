local function get_12_batteries(bank)
	-- Thanks to u/Then-Government-5460 for the hints to this problem
	assert(type(bank) == "string")

	local bad_batteries = #bank - 12
	while bad_batteries > 0 do
		for i = 1, #bank do
			if bank:sub(i, i) < bank:sub(i + 1, i + 1) then
				bank = bank:sub(1, i - 1) .. bank:sub(i + 1)
				break
			end
		end

		bad_batteries = bad_batteries - 1
	end

	return tonumber(bank:sub(1, 12))
end

local function get_2_batteries(bank)
	assert(type(bank) == "string")

	local best = 0
	local sptr = 1
	local fptr = 2

	while fptr <= #bank do
		local f = bank:sub(fptr, fptr)
		local s = bank:sub(sptr, sptr)

		if tonumber(s .. f) > best then
			best = tonumber(s .. f, 10)
		end

		if tonumber(f) >= tonumber(s) then
			sptr = fptr
		end

		fptr = fptr + 1
	end

	-- print(bank, "-->", best)
	return best
end

local function main()
	local part1 = 0
	local part2 = 0

	for bank in io.lines("puzzle.txt") do
		part1 = part1 + get_2_batteries(bank)
		part2 = part2 + get_12_batteries(bank)
	end

	print("Part 1:", part1)
	print("Part 2:", part2)
end

main()
