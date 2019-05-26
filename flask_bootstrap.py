from app import bootstrap_app, db

app = bootstrap_app()  # Initialise the Flask app


@app.shell_context_processor
def make_shell_context():
    """
    Make sqlalchemy db object available to the cli, enables us to run db migrations as follows:
    > flask db init       # Initialise migrations
    > flask db migrate    # Create migration
    > flask db upgrade    # Upgrade the database
    > flask db downgrade  # Downgrade the database by 1 migration
    """
    return {'db': db}
