import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.usefixtures("login")
class TestNavigateMyinfo:

    def test_navigate_dashboard_myinfo(self,login):
        """Test navigating to 'My Info' after login."""
        dashboard_page = DashboardPage(login)  # Using the logged-in session (from the login fixture)

        # Navigate to 'My Info' after login
        dashboard_page.navigate_to_MyInfo()

    def test_verify_myinfo_loaded(self,login):
        """Test verifying that 'My Info' has successfully loaded."""
        dashboard_page = DashboardPage(login)
        dashboard_page.verify_MyInfo()

        # Optionally assert the expected URL or elements
        expected_url = "YOUR_EXPECTED_URL_FOR_MYINFO"
        assert login.current_url == expected_url, f"Expected URL to be {expected_url}, but got {login.current_url}"

