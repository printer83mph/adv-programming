function calc()
	print("Enter a number, 'add', or 'mul': ")
	local inlist = {}
	while true do
		local input = io.read()
		if tonumber(input) ~= nil then
			table.insert(inlist,tonumber(input))
		elseif input == "add" then
			out = 0
			for key,val in pairs(inlist) do
				out = out + val
			end
			break
		elseif input == "mul" then
			out = 1
			for key,val in pairs(inlist) do
				out = out * val
			end
			break
		end
	end
	print(out)
end

calc()