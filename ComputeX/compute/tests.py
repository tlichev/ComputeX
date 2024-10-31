

import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Result

from django.contrib.auth.models import User



@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="password")




@pytest.mark.django_db
def test_compute_view_division_by_zero_error(client, user):
    client.login(username="testuser", password="password")

    csv_content = b"A,O,B\n8,/,0"
    csv_file = SimpleUploadedFile("test.csv", csv_content, content_type="text/csv")

    response = client.post(reverse("compute"), {"file": csv_file})

    assert response.status_code == 200
    assert "error" in response.context
    assert "Division by zero" in response.context["error"]

    assert Result.objects.count() == 0


@pytest.mark.django_db
def test_compute_view_unsupported_operator_error(client, user):
    client.login(username="testuser", password="password")

    csv_content = b"A,O,B\n1,^,2"
    csv_file = SimpleUploadedFile("test.csv", csv_content, content_type="text/csv")

    response = client.post(reverse("compute"), {"file": csv_file})

    assert response.status_code == 200
    assert "error" in response.context
    assert "Unsupported operator" in response.context["error"]

    assert Result.objects.count() == 0


@pytest.mark.django_db
def test_compute_view_invalid_data_format_error(client, user):
    client.login(username="testuser", password="password")

    csv_content = b"A,O,B\none,+,two"
    csv_file = SimpleUploadedFile("test.csv", csv_content, content_type="text/csv")

    response = client.post(reverse("compute"), {"file": csv_file})

    assert response.status_code == 200
    assert "error" in response.context
    assert "Invalid data format" in response.context["error"]

    assert Result.objects.count() == 0


@pytest.mark.django_db
def test_compute_view_no_file_uploaded_error(client, user):
    client.login(username="testuser", password="password")

    response = client.post(reverse("compute"), {})

    assert response.status_code == 200
    assert "error" in response.context
    assert response.context["error"] == "Please upload a valid CSV file."
