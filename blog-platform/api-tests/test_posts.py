import requests
import time

class TestPosts:
    """ Test posts endpoints """
    def validate_post_structure(self, posts):
        required_fields = ["id", "title", "content", "author", "createdAt"]

        # Validate only the first 10 posts
        posts_to_validate = posts[:10]  # This takes first 10 or all if less than 10

        for post in posts_to_validate:
            for field in required_fields:
                assert field in post, f"Missing required field: {field}"
        

    def test_get_all_posts(self, base_url):
        """ Testing getting all posts without authentication """
        response = requests.get(f"{base_url}/posts")

        assert response.status_code == 200
        # This checks if the converted object is an instance of a Python list
        assert isinstance(response.json(), list)
        
        posts = response.json()
        assert posts is not None
        
        self.validate_post_structure(posts)
    

    






    
    
        