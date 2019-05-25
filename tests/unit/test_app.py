from app import bootstrap_app


class TestApp:

    @classmethod
    def setup_class(cls):
        # Setup class wide Flask app context so we can access Flask app fields
        cls.app = bootstrap_app()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

    @classmethod
    def teardown_class(cls):
        cls.ctx.pop()  # Remove Flask app context

    def test_app_is_bootstrapped(self):
        """ Test to demonstrate flask app is instantiated correctly """
        app = bootstrap_app()

        logdir = app.config['LOG_DIR']

        assert logdir == 'logs'
