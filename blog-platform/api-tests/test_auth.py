import requests
import time


class TestAuthentication:
    """ Test authentication endpoints """

    def test_register_user_success(self, base_url):
        """ Test successful user registration """
        user_data = {
            "email": f"test-{int(time.time())}@example.com",
            "password": "password123"
        }

        response = requests.post(f"{base_url}/auth/register", json=user_data)

        assert response.status_code == 200
        assert "token" in response.json()
        assert "expiresIn" in response.json()
        assert response.json()["expiresIn"] == 86400

    
    


        
