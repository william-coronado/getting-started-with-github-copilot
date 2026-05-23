from src.app import activities


def test_signup_appends_participant_and_returns_message(client):
    # Arrange
    email = "new.student@mergington.edu"
    activity_name = "Chess Club"
    expected_message = {"message": f"Signed up {email} for {activity_name}"}

    assert email not in activities[activity_name]["participants"]

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_message
    assert email in activities[activity_name]["participants"]
