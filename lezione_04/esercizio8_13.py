def build_profile(first_name, last_name, **attributes):
    profile = f"{first_name} {last_name}"
    
    for key, value in attributes.items():
        profile += f", {key} {value}"
    
    return profile

profile = build_profile("Andrea", "Giumi", age=27, hair="Brown", weight="1.76")

print(profile)
