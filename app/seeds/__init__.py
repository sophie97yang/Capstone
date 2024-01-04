from flask.cli import AppGroup
from .users import seed_users, undo_users
from .trips import seed_trips,undo_trips
from .expenses import seed_expenses,undo_expenses
from .bookings import seed_bookings,undo_bookings,undo_itineraries

from ..models import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()

    users = seed_users()
    trips = seed_trips(users)
    seed_expenses(users,trips)
    seed_bookings()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_itineraries()
    undo_bookings()
    undo_expenses()
    undo_trips()
    undo_users()

    # Add other undo functions here
