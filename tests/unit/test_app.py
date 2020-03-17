class TestApp:
    def test_app_is_bootstrapped(self, app):
        """ Test to demonstrate flask app is instantiated correctly """
        logdir = app.config["LOG_DIR"]

        assert logdir == "logsdd"
