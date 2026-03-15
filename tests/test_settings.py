from settings import Settings


def test_settings_loaded_correctly():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ipum-lab-test"
    assert settings.API_KEY == "fake-test-key"
    assert settings.DATABASE_PASSWORD == "fake-db-pass"
    assert settings.TOKEN == "fake-token"
