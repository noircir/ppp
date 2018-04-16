def extract_full_name(list_of_dicts):
    return [" ".join(t) for t in list(zip([d["first"] for d in list_of_dicts], [d["last"] for d in list_of_dicts]))]
    # return [" ".join(t) for t in list(zip([d.get("first") for d in list_of_dicts], [d.get("last") for d in list_of_dicts]))]

print(extract_full_name([{'first':'elena', 'last':'kolmogorova'}, {'first':'sigourney', 'last':'wamback'}]))