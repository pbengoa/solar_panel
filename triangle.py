## We can asume that panel_a and panel_b are numbers higher than 0
## We can asume that roof_x and roof_y are numbers higher than 0

import sys
import math

def get_amount(bigger_side, smaller_side, roof_x, roof_h, angle_sides):
  excess_x = smaller_side / math.tan(angle_sides) * 2
  
  amount = 0
  rest_space_x = roof_x - excess_x
  rest_space_h = roof_h
  
  if rest_space_x <= 0:
    return 0

  if smaller_side <= rest_space_h:
    amount = rest_space_x // bigger_side
  
  return (amount, rest_space_x)
  

def max_rectangles(panel_a, panel_b, roof_x, roof_h):
  total_amount = 0
  rest_space_x = roof_x
  rest_space_h = roof_h
  angle_sides = math.atan(roof_h / (roof_x/2))
  
  check_horizontal = False
  check_vertical = False
  
  while not check_horizontal or not check_vertical:
    if not check_horizontal:
      amount_horizontal, excess = get_amount(panel_a, panel_b, rest_space_x, rest_space_h, angle_sides)
      if check_horizontal:
        break
      if amount_horizontal == 0:
        check_horizontal = True
        panel_a, panel_b = panel_b, panel_a
      else:
        total_amount += amount_horizontal
        rest_space_x -= excess
        rest_space_h -= panel_b
        
  return total_amount

[panel_a, panel_b, roof_x, roof_y] = sys.argv[1:]
max_rectangles_amount = max_rectangles(int(panel_a), int(panel_b), int(roof_x), int(roof_y))

print(f"Max rectangles that fit in the roof: {max_rectangles_amount} rectangles.")

