import pytest
import os


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate /var/lib/jenkins/workspace/auto-test（git）/temps -o /var/lib/jenkins/workspace/auto-test（git）/reports --clean")