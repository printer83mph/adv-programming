function calc()
	print("Enter a number, 'add', or 'mul': ")
	local inlist = {}
	while true do
		local input = io.read()
		if tonumber(input) ~= nil then
			table.insert(inlist,tonumber(input))
		elseif input == "add" then
			local out = 0
			for key,val in pairs(inlist) do
				out = out + val
			end
			print(out)
			break
		elseif input == "mul" then
			local out = 1
			for key,val in pairs(inlist) do
				out = out * val
			end
			print(out)
			break
		end
	end
end

calc()