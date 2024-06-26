import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from config import get_settings

from . import validators
from . import security

settings = get_settings()


class User(Model):
    __keyspace__ = settings.astradb_keyspace
    email = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"

    def set_password(self, pw, commit=False):
        pw_hash = security.generate_hash(pw)
        self.password = pw_hash
        if commit:
            self.save()
        return True

    def verify_password(self, pw_str):
        pw_hash = self.password
        verified, _ = security.verify_hash(pw_hash, pw_str)
        return verified

    @staticmethod
    def create_user(email, password=None):
        q = User.objects.filter(email=email)
        if q.count() != 0:
            raise Exception("User already has an account.")
        valid, msg, email = validators._validate_email(email)
        if not valid:
            raise Exception(f"Invalid email: {msg}")
        obj = User(email=email)
        obj.set_password(password, commit=True)
        return obj
