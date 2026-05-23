def test_get_activities_returns_expected_keys(client):
    # Arrange
    expected_keys = {"Chess Club", "Programming Class", "Gym Class"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert expected_keys.issubset(data.keys())
