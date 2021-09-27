num_people = int(input("how many people are there "))
num_pizza = input("how many pizzas are there ")
slices_per_pizza = int(input("how many slices are there "))
cost_per_pizza = float(input("how much does each pizza cost "))

total_slices = num_pizza * slices_per_pizza
slices_per_person = total_slices / num_people

print(f"there are (slices_per_person:.1f) slices per person")