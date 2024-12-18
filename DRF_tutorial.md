# Quickstart: Building a Django REST Framework API on Windows 11 (Using PowerShell, VS Code, and Django REST Framework)

This guide will walk you through creating a simple API that allows admin users to view and edit the users and groups in the system. All instructions are tailored for a Windows 11 environment using PowerShell and VS Code.

---

## **Project Setup**

### 1. Create the Project Directory
Open PowerShell and run the following commands:
```powershell
mkdir mytutorial
cd mytutorial
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
```powershell
python -m venv env
.\env\Scripts\activate
```

You should now see `(env)` at the start of your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies
Install Django and Django REST Framework:
```powershell
pip install django djangorestframework
```

### 4. Create a Django Project
Create a new Django project named `mytutorial` in the current directory:
```powershell
django-admin startproject mytutorial .
```

### 5. Create an App
Navigate into the project directory and create a new app called `quickstart`:
```powershell
cd mytutorial
django-admin startapp quickstart
cd ..
```

Your project structure should now look like this:
```
.
./mytutorial
./mytutorial/asgi.py
./mytutorial/__init__.py
./mytutorial/settings.py
./mytutorial/urls.py
./mytutorial/wsgi.py
./quickstart
./quickstart/migrations
./quickstart/migrations/__init__.py
./quickstart/admin.py
./quickstart/apps.py
./quickstart/models.py
./quickstart/tests.py
./quickstart/views.py
./manage.py
./env
```

---

## **Database Initialization**

### 1. Migrate the Database
Run the following command to set up the database:
```powershell
python manage.py migrate
```

### 2. Create a Superuser
Create an admin user for authentication:
```powershell
python manage.py createsuperuser --username admin --email admin@example.com
```
Follow the prompts to set a password.

---

## **Define Serializers**
Create a new file named `serializers.py` in the `quickstart` app directory:
```powershell
ni .\quickstart\serializers.py
```

Add the following code to `serializers.py`:
```python
from django.contrib.auth.models import Group, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```

---

## **Create Views**
Open `views.py` in the `quickstart` app directory and add the following code:
```python
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from quickstart.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

---

## **Configure URLs**
Edit `urls.py` in the `mytutorial` directory:
```python
from django.urls import include, path
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

---

## **Add Pagination**
Edit `settings.py` in the `mytutorial` directory to enable pagination:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

Also, add `rest_framework` to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## **Test the API**

### 1. Run the Development Server
Start the server:
```powershell
python manage.py runserver
```

### 2. Access the API
- **In the browser**: Visit [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/).
- **Using `httpie`**:
   ```powershell
   pip install httpie
   http -a admin http://127.0.0.1:8000/users/
   ```
- **Using `curl`**:
   ```powershell
   curl -u admin -H "Accept: application/json; indent=4" http://127.0.0.1:8000/users/
   ```

You should see JSON output for the users in your system.

---

Congratulations! You've successfully set up a Django REST Framework project with PowerShell and VS Code on Windows 11. Let me know if you need further assistance or have questions! 😊


