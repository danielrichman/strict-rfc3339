Strict, simple, lightweight RFC3339 functions
=============================================

Goals
-----

 - Convert unix timestamps to and from RFC3339.
 - Either produce RFC3339 strings with a UTC offset (Z) or with the offset
   that the C time module reports is the local timezone offset.
 - Simple with minimal dependencies/libraries.
 - Avoid timezones as much as possible.
 - Be very strict and follow RFC3339 as closely as possible.

Caveats
-------

 - Leap seconds are not quite supported, since timestamps do not support them,
   and it requires access to timezone data.
 - You may be limited by the size of time_t on 32 bit systems.

In both cases, see 'Notes' below.

Rationale, comparisons to other choices
---------------------------------------

(Not in any way meant to be aggressive, merely providing my observations)

 - Other libraries have trouble with DST transitions and ambiguous times.
 - Generally, using the python datetime object seems to be more trouble than
   it's worth, introducing problems with timezones. Further, they don't support
   leap seconds (timestamps don't either, but it's still a bit disappointing).
 - The excellent pytz library does timezones perfectly, however it didn't (at
   the time of writing have a method for getting the local timezone or the
   'now' time in the local zone.
 - (anecdotal observation): other libraries suffer DST problems (etc.) because
   of information lost when converting or transferring between two libraries
   (e.g., time -> datetime loses DST info in the tuple)

The things powering these functions
-----------------------------------

These functions are essentially string and integer operations only. A very 
small number of functions do the heavy lifting. These come from two modules:
time and calendar.

time is a thin wrapper around the C platform's time libraries. This is good
because these are most likely of high quality and always correct. From the
time library, we use:

 - time: (actually calls gettimeofday) provides 'now' -> timestamp
 - gmtime: splits a timestamp into a UTC time tuple
 - localtime: splits a timestamp into a local time tuple
   _including_ the 'is DST' flag
 - timezone: variable that provides the local timezone offset
 - altzone: variable that provides the local timezone DST offset

Based on the (probably correct) assumption that gmtime and localtime are
always right, we can use gmtime and localtime, and take the difference in order
to figure out what the local offset is. As clunky as it sounds, it's far easier
than using a fully fledged timezone library.

calendar is implemented in python. From calendar, we use

 - timegm: turns a UTC time tuple into a timestamp. This essentially just
   multiplies each number in the tuple by the number of seconds in it. It
   does use datetime.date to work out the number of days between Jan 1 1970
   and the ymd in the tuple, but that should be OK. It does not perform much
   validation at all.
 - monthrange: gives the number of days in a (year, month). I checked and
   (atleast in my copy of python 2.6) the function used for leap years is
   identical to the one specified in RFC3339.

Notes
-----

 - RFC3339 specifies an offset, not a timezone. Timezones are evil and will
   make you want to hurt yourself.
 - Although slightly roundabout, it might be simpler to consider RFC3339
   times as a human readable method of specifying a moment in time (only).
   Sure, there can be many RFC3339 strings that represent one moment in time,
   but that doesn't really matter.
   An RFC3339 string represents a moment in time unambiguously and you do
   not need to consult timezone data in order to work out the UTC time
   represented by a RFC3339 time.
   Really, these functions merely provide a way of converting RFC3339 times to
   exactly equivalent integers/floats and back.
 - Note that timestamps don't support leap seconds: a day is always 86400.
   Also, validating leap seconds is extra difficult, because you'd to access
   to up-to-date tzdata.
   For this reason strict_rfc3339 does not support leap seconds: in validation,
   seconds == 60 or seconds == 61 are rejected.
   In the case of reverse leap seconds, calendar.timegm will blissfully accept
   it. The result would be about as correct as you could get.
 - RFC3339 generation using gmtime or localtime may be limited by the size
   of time_t on the system: if it is 32 bit, you're limited to dates between
   (approx) 1901 and 2038. This does not affect rfc3339_to_timestamp.
