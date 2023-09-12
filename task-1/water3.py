def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)

def successors(s):
    x, y, z = s
    
    if y > 0 and x < 8:  # 5->8
        t = min(y, 8 - x)
        yield ((x + t, y - t, z), t)
		
    if x > 0 and y < 5:  # 8->5
        t = min(x, 5 - y)
		yield ((x - t, y + t, z), t)
	
	
    if z > 0 and x < 8:  # 3->8
        t = min(z, 8 - x)
        yield ((x + t, y, z - t), t)

    if x > 0 and z < 3:  # 8->3
        t = min(x, 3 - z)
        yield ((x - t, y, z + t), t)


	if z > 0 and y < 5:  # 3->5
        t = min(z, 5 - y)
        yield ((x, y + t, z - t), t)

    if y > 0 and z < 3:  # 5->3
        t = min(y, 3 - z) 
        yield ((x, y - t, z + t), t)
