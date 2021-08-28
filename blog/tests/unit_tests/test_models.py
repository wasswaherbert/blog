import pytest
from blog.models import Post,User
"""
we use the @pytest.mark.django_db (decorator) to access the database when running our tests
After creating a new user and post with valid arguments to the constructor, 
the properties of the created post are checked to make sure it was created properly.
"""
@pytest.mark.django_db
def test_create_post(create_user,create_post):
    assert create_post.title == "Simple article"
    assert create_post.slug == "spo"
    assert create_post.author == create_user
    assert create_post.body == "my first blog post"

@pytest.mark.django_db
def test_create_comment(create_post,create_comment):
    assert create_comment.post == create_post
    assert create_comment.name == "sean"
    assert create_comment.email == "seankamugasa@gmail.com"
    assert create_comment.body == "this is a good blog"
    
	    

