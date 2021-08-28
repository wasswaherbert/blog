import pytest
from blog.forms import EmailPostForm,CommentForm,SearchForm
@pytest.mark.django_db
def test_valid_emailpostform():
	data = {'name':'wasswa','email':'herbert@gmail.com','to':'seankamugasa@gmail.com','comments':'good'}
	form = EmailPostForm(data=data)
	assert form.is_valid()

@pytest.mark.django_db
def test_invalid_emailpostform():
	data = {'name':'wasswa','email':'herbert@gmail.com','to':'seankamugasa@gmail.com','comments':''}
	form = EmailPostForm(data=data)
	assert  form.is_valid()

@pytest.mark.django_db
def test_valid_commentform(create_comment):
	data = {'name':'wasswa','email':'herbert@gmail.com','body':'good work guys'}
	form = CommentForm(data=data)
	assert form.is_valid()

@pytest.mark.skip
@pytest.mark.django_db
def test_invalid_commentform(create_comment):
	data = {'name':'wasswa','email':'herbert@gmail.com','body':''}
	form = CommentForm(data=data)
	assert form.is_valid()

@pytest.mark.django_db
def test_valid_searchform(create_post,create_user):
	data = {'query':'django'}
	form = SearchForm(data=data)
	assert form.is_valid()