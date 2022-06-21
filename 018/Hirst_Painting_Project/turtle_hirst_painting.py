import colorgram

colors = colorgram.extract('/Users/MichelleA/repos/100-Days/018/Hirst_Painting_Project/hirst_painting.jpg', 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.g) for color in colors]

print(color_list)