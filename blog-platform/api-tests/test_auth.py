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
    

    def test_register_user_invalid_email(self, base_url):
        """Test registration with invalid email format"""
        user_data = {
            "email": "invalid-email",
            "password": "password123"
        }

        response = requests.post(f"{base_url}/auth/register", json=user_data)
        
        assert response.status_code == 400
        assert "Invalid email format" in response.text

    
    def test_register_user_missing_password(self, base_url):
        """Test registration with missing password"""
        user_data = {
            "email": "test@example.com"
            # Missing password
        }
        
        response = requests.post(f"{base_url}/auth/register", json=user_data)
        
        assert response.status_code == 400
        assert "Password is required" in response.text
    

    def test_login_user_success(self, base_url):
        """Test successful user login"""
        # First register a user
        user_data = {
            "email": f"test-login-success-{int(time.time())}@example.com",
            "password": "password123"
        }
        
        register_response = requests.post(f"{base_url}/auth/register", json=user_data)
        assert register_response.status_code == 200
        
        # Then login with the same credentials
        login_response = requests.post(f"{base_url}/auth/login", json=user_data)
        
        assert login_response.status_code == 200
        assert "token" in login_response.json()
        assert "expiresIn" in login_response.json()
    

    def test_login_user_invalid_credentials(self, base_url):
        """Test login with invalid credentials"""
        user_data = {
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }
        
        response = requests.post(f"{base_url}/auth/login", json=user_data)
        print(response.json())
        
        assert response.status_code == 401
        assert "Incorrect username or password" in response.text
    

    def test_register_duplicate_email(self, base_url):
        """Test registration with duplicate email"""
        user_data = {
            "email": f"test-register-duplicate-{int(time.time())}@example.com",
            "password": "password123"
        }
        
        # Register first time
        response1 = requests.post(f"{base_url}/auth/register", json=user_data)
        assert response1.status_code == 200
        
        # Try to register with same email
        response2 = requests.post(f"{base_url}/auth/register", json=user_data)
        print(response2.json())
        
        # Should fail with duplicate email error
        assert response2.status_code == 409

    
    


        
