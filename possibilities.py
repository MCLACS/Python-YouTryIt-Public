colors = ["blue", "red", "green"]
textures = ["smooth", "bumpy"]
shapes = ["circle", "square", "triangle"]

p = []
for color in colors: # 3 times
    for texture in textures: # 2 times
        for shape in shapes: # 3 times
            p.append("%s %s %s" % (color, texture, shape))

print len(p)
print p
    

