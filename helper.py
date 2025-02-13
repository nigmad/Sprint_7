

def modify_login_body_for_empty_fields(fields_to_check, generate_courier_fixture):
    modified_bodies = []
    for field in fields_to_check:
        login_data = {key: generate_courier_fixture.get(key) if key != field else "" for key in fields_to_check}
        modified_bodies.append(login_data)
    return modified_bodies
