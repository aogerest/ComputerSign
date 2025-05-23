# Premier-League-24/25
## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.10.5``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Install MySQL
Install ```mysql-8.0.29```. Follow the steps form the below reference document based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)
#### 3. Setup virtual environment
```bash
# Install virtual environment
#sudo pip install virtualenv

# Make a directory
#mkdir envs

# Create virtual environment
#virtualenv ./envs/
#或者
#python3.10 -m venv ./envs/

# Activate virtual environment
#source envs/bin/activate
```

#### 4. Clone git repository
```bash
git clone "https://github.com/Vatus118/Django-Pro.git"
git checkout master
```

#### 5. Install requirements
```bash
cd Django-Pro/
pip install -r requirements.txt
```

#### 6. Load sample data into MySQL
```bash
# open mysql bash
mysql -u <mysql-user> -p

# Give the absolute path of the file
mysql> source ~/Django-Pro/PremierLeague.sql
mysql> exit;

```
#### 7. Edit project settings
```bash
# open settings file
vim panorbit/settings.py

# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'world',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}

# Edit email configurations.
# Search for email configurations
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-email-password>'
EMAIL_PORT = 587

# save the file
```
#### 8. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

mysql -u <mysql-user> -p

# Give the absolute path of the file
mysql> source /world_team.sql
mysql> source /world_statistic.sql
mysql> source /world_standing.sql
mysql> source /world_score.sql
mysql> source /world_player.sql
mysql> source /world_match.sql
mysql> source /world_details.sql
mysql> exit;

# For search feature we need to index certain tables to the haystack. For that run below command.
python manage.py rebuild_index

# Run the server
python manage.py runserver localhost:8001

# your server is up on port 8001
```
Try opening [http://localhost:8001](http://localhost:8001) in the browser.
Now you are good to go.