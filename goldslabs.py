gold_slabs = [
    {"from":0.500,"to":1.500,"wastage":0.200,"making":150},
    {"from":1.500,"to":3.500,"wastage":0.400,"making":200},
    {"from":3.500,"to":5.500,"wastage":0.800,"making":400},
    {"from":5.500,"to":7.500,"wastage":1.200,"making":550},
    {"from":7.500,"to":9.500,"wastage":1.280,"making":700},
    {"from":15.500,"to":17.000,"wastage":2.540,"making":850},
    {"from":23.500,"to":25.000,"wastage":3.820,"making":1000}
]
print("--GOLD DETAILS--")
wastage_list =[
    f"{g['from']}gram-{g['to']}gram :{g['wastage']}gram wastage"
    for g in gold_slabs
    ]
making_charges_list=[
    f"{g['from']}gram-{g['to']}gram :{g['making']}making charges"
    for g in gold_slabs
]
print("\nWASTAGE DETAILS:")
for w in wastage_list:
    print(w)
print("\nMAKING CHARGES DETAILS:")
for m in making_charges_list:
    print(m)
    
