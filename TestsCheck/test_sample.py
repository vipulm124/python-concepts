import pytest
from datetime import datetime
from freezegun import freeze_time

@freeze_time('2012-01-14 16:00:00+02:00')
def test_datetime_now():
    print('printing something here')
    now = datetime.now()
    print(f"Current datetime is: {now}")
    now_astimezone = now.astimezone()
    now_withouttimezone = now.replace(tzinfo=None)
    assert isinstance(now, datetime)

if __name__ == "__main__":
    pytest.main(['-s', __file__])

    