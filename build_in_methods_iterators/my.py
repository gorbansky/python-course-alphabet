print('Hi')

distance = 25

reduce_values = [{"reduce_level": 50,
                          "distance": 100,
                          },

                         {"reduce_level": 25,
                          "distance": 200
                          },

                         {"reduce_level": 15,
                          "distance": 50
                          },

                         {"reduce_level": 5,
                          "distance": 25
                          },

                         {"reduce_level": 2,
                          "distance": 0
                          }]

for i in reduce_values:
    #if i["distance"] < distance:
    print(i["reduce_level"])
        #break
print (f"Your cat ran {distance} kilometers")

print(reduce_values)
