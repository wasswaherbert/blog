from blog.models import Post,User,Comment
import pytest
"""
we use @pytest.fixture, to create a fixture that creates a user,post and comment objects 
so that their associated test functions are reduced to the assert statements only.
"""
@pytest.fixture
def create_user():
	"""We create a new user with valid arguments to the constructor and return the user object"""
	user = User.objects.create(username="kelvin")
	return user

@pytest.fixture
def create_post(create_user):
	"""We create a new post with valid arguments to the constructor and return the post object"""
	post = Post.objects.create(
		title="Simple article",slug = "spo",author = create_user,body = "my first blog post")
	return post

@pytest.fixture
def create_comment(create_post):
	"""We create a new comment with valid arguments to the constructor and return the comment object"""
	comment= Comment.objects.create(
		post=create_post,name="sean",email="seankamugasa@gmail.com",body="this is a good blog")
	return comment
