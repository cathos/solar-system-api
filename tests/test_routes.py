# from hello-books

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_handle_teapot(client):
    response = client.get("/planets/teapot")

    assert response.status_code == 418

def test_get_one_planet(client, two_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 3,
        "name": "Earth",
        "order_from_sun": 3,
        "description": "something about earth",
        "gravity": "9.81 m/s2"
    }

def test_get_all_planets(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 3,
        "name": "Earth",
        "order_from_sun": 3,
        "description": "something about earth",
        "gravity": "9.81 m/s2"},
        {"id": 2, 
        "name": "Venus", 
        "order_from_sun":2,
        "description":"Very hot planet with a dense atmosphere",
        "gravity": "8.87 m/s2"}
    ]



def test_get_invalid_planet(client):
    response = client.get("planets/12")
    response_body = response.get_json()

    assert response.status_code == 404

def test_post_one_planet_to_database(client):
    response = client.post("/planets", json = {
        "name": "Pluto", 
        "order_from_sun": 9,
        "description": "Pluto is smaller than Earth's moon",
        "gravity": "0.62 m/s2" 
        })
    response_body = response.get_json()
    
    assert response.status_code == 201
    print(response_body)
    assert response_body == b"Planet Pluto successfully created"   


