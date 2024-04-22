## We can asume that panel_a and panel_b are numbers higher than 0
## We can asume that roof_x and roof_y are numbers higher than 0

import sys


def get_best_fit(panel_a, panel_b, roof_x, roof_y):
    best_fit = 100000000000
    amount = 0
    rep_x = 0
    rep_y = 0
  
    if panel_a <= roof_x and panel_b <= roof_y:
      best_fit = roof_x % panel_a 
      amount = roof_x // panel_a
      rep_x = 0
      rep_y = panel_b
    
    if panel_b <= roof_x and panel_a <= roof_y and best_fit > roof_x % panel_b :
      best_fit = roof_x % panel_b
      amount = roof_x // panel_b
      rep_x = panel_a
      rep_y = 0
    return (amount, rep_x, rep_y, best_fit)

def max_rectangles(panel_a, panel_b, roof_x, roof_y):
  total_amount = 0
  rest_space_x = roof_x
  rest_space_y = roof_y
  
  while True:
    amount, rep_x, rep_y, best_fit = get_best_fit(panel_a, panel_b, rest_space_x, rest_space_y)
    amount_2, rep_x_2, rep_y_2, best_fit_2 = get_best_fit(panel_a, panel_b, rest_space_y, rest_space_x)
    if best_fit_2 <= best_fit and amount_2 > amount:
      amount = amount_2
      rep_x = rep_x_2
      rep_y = rep_y_2
      
    if amount == 0:
      break
    
    total_amount += amount
    
    rest_space_x = rest_space_x - rep_x
    rest_space_y = rest_space_y - rep_y
    print(f"Amount: {amount}, rep_x: {rep_x}, rep_y: {rep_y}, best_fit: {best_fit}, rest_space_x: {rest_space_x}, rest_space_y: {rest_space_y}")

  return total_amount
  


[panel_a, panel_b, roof_x, roof_y] = sys.argv[1:]

max_rectangles_amount = max_rectangles(int(panel_a), int(panel_b), int(roof_x), int(roof_y))

print(f"Max rectangles that fit in the roof: {max_rectangles_amount} rectangles.")