from __future__ import division

from datetime import timedelta, tzinfo

class FixedOffset(tzinfo):
    '''
    Represent a timezone with a fixed offset from UTC and no adjustment for
    DST.

    >>> FixedOffset(4,0)
    <UTC+04:00>
    >>> FixedOffset(-4,0)
    <UTC-04:00>
    >>> FixedOffset(4,30)
    <UTC+04:30>

    The class tries to do the right thing with the sign of the time zone offset:

    >>> FixedOffset(-9,30)
    <UTC-09:30>
    >>> FixedOffset(-9,-30)
    Traceback (most recent call last):
    ...
    ValueError: minutes must not be negative

    Offsets must thus be normalized so that the minute value is positive:

    >>> FixedOffset(-8,30)
    <UTC-08:30>

    '''

    def __init__(self, hours, minutes):
        '''
        Create a new FixedOffset instance with the given offset.

        '''
        tzinfo.__init__(self)
        if minutes < 0:
            raise ValueError("minutes must not be negative")
        if hours < 0:
            minutes *= -1
        self.__offset = timedelta(hours = hours,
                                  minutes = minutes)
        self.__name = "UTC%s" % (timezone(timedelta_seconds(self.__offset)))

    def dst(self, dt):
        '''
        Return offset for DST.  Always returns timedelta(0).

        '''
        return timedelta(0)
    
    def utcoffset(self, dt):
        '''
        Return offset from UTC.

        '''
        return self.__offset
    
    def tzname(self, dt):
        '''
        Return name of timezone.
        
        '''
        return self.__name
    
    def __repr__(self):
        return "<%s>" % self.tzname(None)


def timedelta_seconds(td):
    '''
    Return the offset stored by a timedelta object as an integer number of
    seconds.  Microseconds, if present, are rounded to the nearest second.

    >>> timedelta_seconds(timedelta(hours=1))
    3600
    >>> timedelta_seconds(timedelta(hours=-1))
    -3600
    >>> timedelta_seconds(timedelta(hours=1, minutes=30))
    5400
    >>> timedelta_seconds(timedelta(hours=1, minutes=30, 
    ... microseconds=300000))
    5400
    >>> timedelta_seconds(timedelta(hours=1, minutes=30,
    ...	microseconds=900000))
    5401

    '''

    days = td.days
    seconds = td.seconds
    microseconds = td.microseconds

    return int(round((days * 86400) + seconds + (microseconds/1000000)))


def timezone(utcoffset):
    '''
    Return a string reprenseting the timezone offset.
    Remaining seconds are rounded to the nearest minute.

    >>> timezone(3600)
    '+01:00'
    >>> timezone(5400)
    '+01:30'
    >>> timezone(-28800)
    '-08:00'

    '''

    hours, seconds = divmod(abs(utcoffset), 3600)
    minutes = round(float(seconds) / 60)

    if utcoffset >= 0:
        return '+%02d:%02d' % (hours, minutes)
    else:
        return '-%02d:%02d' % (hours, minutes)
