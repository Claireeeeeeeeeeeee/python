# list datastructure, it is ordered and changeable
cars = ["Mercedes", "Nissan", "Toyota", "Rangerover"]
cars[1] = "Subaru"
cars.append("Mitsubishi")
cars.insert(2, "BMW")
cars.pop(3)
# cars.sort(reverse=0)
# cars.sort(key=0)
cars.sort()
cars.reverse()
print(cars)
# cars.copy()
# this is a tuple ,ordered it is unchangeable
fruits = ("Mangoes", "Oranges", "Pineapple", "Avocado")
print(fruits)
for f in fruits:
    print(f)

    #sets datastructures,unordered
countries={"Kenya","Uganda","Tanzania","Burundi","Ethiopia"}
print(countries)

  #Dictionaries
matunda={
    "amount":40,
    "jina":"ndizi",
    "rangi":"manjano",
    "smell":"good",
}
matunda["size"]="Large"
matunda.pop("rangi")
print(matunda)



