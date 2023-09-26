# The function estimate_insurance_cost() estimates the medical insurance cost for an
# individual, based on five variables --
    # age
    # sex: 0 for female, 1 for male
    # bmi
    # num_of_children
    # smoker: 0 for non-smoker, 1 for smoker

# Function to estimate insurance cost --
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Cindy's insurance cost estimate --
cindy_insurance_cost = estimate_insurance_cost(name = "Cindy", age = 25, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Jose's insurance cost estimate --
jose_insurance_cost = estimate_insurance_cost(name = "Jose", age = 35, sex = 1, bmi = 36.3, num_of_children = 6, smoker = 0)

# Jennifer's insurance cost estimate --
jennifer_insurance_cost = estimate_insurance_cost(name = "Jennifer", age = 19, sex = 0, bmi = 18.3, num_of_children = 0, smoker = 1)

# OUTPUT: Cindy's Estimated Insurance Cost: 2722.0 dollars.
# OUTPUT: Jose's Estimated Insurance Cost: 12103.0 dollars.    
# OUTPUT: Jennifer's Estimated Insurance Cost: 23021.0 dollars.

# Now I want to compare the estimated insurance costs, as calculated by the function, to 
# the actual amounts that Cindy, Jose, and Jennifer paid.

names = ["Cindy", "Jose", "Jennifer"]
insurance_costs = [2650.0, 12000.0, 22750.0]

insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data: " + str(insurance_data))

estimated_insurance_data = []

estimated_insurance_data.append(("Cindy", cindy_insurance_cost))
estimated_insurance_data.append(("Jose", jose_insurance_cost)) 
estimated_insurance_data.append(("Jennifer", jennifer_insurance_cost))

# OUTPUT: Here is the actual insurance cost data: [('Cindy', 2650.0), ('Jose', 12000.0), ('Jennifer', 22750.0)]

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

# OUTPUT: Here is the estimated insurance cost data: [('Cindy', 2722.0), ('Jose', 12103.0), ('Jennifer', 23021.0)]

# BEHOLD! As you’ve seen, lists are data structures in Python 
# that can contain multiple pieces of data in a single object.
