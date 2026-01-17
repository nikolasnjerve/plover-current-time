# Current time
### obs! dette er en fork direkte fra Emily sin Current time. jeg har endret python scriptet sånn at det skriver ut norsk dato og tid. For å få den til å virke må du laste ned. tzdata. for å gjøre det må du åpne Powershell og skrive "Pip install tzdata" så erstatter du current time filen i pluginen (gå inn i config  folderen via plover. Og finn den under Win 313/site packages..) med den som ligger her.

# beskrivelse fra Emily
> Plover plugin for inserting the current time in an `strftime()` format

This can be used to indicate the current time when writing, useful for keeping track of when a transcription started, or when notible events occur; such as breaks.

## Installation

Install from the Plover plugins manager.

## Usage and Examples


du kan definere hvilken stenografi "outline" du vil for dette, men du må følge oppskriften på oversettelsen som står under.

| Dictionary Entry | Description |
| ---- | ---- |
| `"T*EUPL": "{:time:%H:%M:%S}",` | Output current time in 24-Hour format. | 
| `"SO*FL": "{:time:%Y-%m-%dT%H:%M:%S.%f%z}",` | Output current time in ISO-8601 format. | 
| `"TKA*ET": "{:time:%A, %d %B, %Y},"` | Output current date in a nice human readable format. |
| `"PWRAEBG": "\n(break started: {:time:%H:%M:%S}{^})\n",` | Note that a break has started and at what time. |
| `"PWRA*EBG": "\n(break ended: {:time:%H:%M:%S}{^})\n",` | Note that the break has ended and at what time. |

## her er forkortelsene du trenger for å få dette til å virke.

| Dictionary Entry | Example | Description |
| ---- | ---- | ---- |
|`%a`|	Sun	|Weekday as locale’s abbreviated name.|
|`%A`|	Sunday |Weekday as locale’s full name.|
|`%w`|	0	| Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.|
|`%d`|	08|	Day of the month as a zero-padded decimal number.|
|`%-d`|	8|	Day of the month as a decimal number. (Platform specific)|
|`%b`|	Sep	| Month as locale’s abbreviated name.|
|`%B`|	September|	|Month as locale’s full name.|
|`%m`|	09	|Month as a zero-padded decimal number.|
|`%-m`|	9	|Month as a decimal number. (Platform specific)|
|`%y`|	13	|Year without century as a zero-padded decimal number.|
|`%Y`|	2013	|Year with century as a decimal number.|
|`%H`|	07	|Hour (24-hour clock) as a zero-padded decimal number.|
|`%-H`|	7	|Hour (24-hour clock) as a decimal number. (Platform specific)|
|`%I`|	07	|Hour (12-hour clock) as a zero-padded decimal number.|
|`%-I`|	7	|Hour (12-hour clock) as a decimal number. (Platform specific)|
|`%p`|	AM	|Locale’s equivalent of either AM or PM.|
|`%M`|	06	|Minute as a zero-padded decimal number.|
|`%-M`|	6	|Minute as a decimal number. (Platform specific)|
|`%S`|	05	|Second as a zero-padded decimal number.|
|`%-S`|	5	|Second as a decimal number. (Platform specific)|
|`%f`|	000000	|Microsecond as a decimal number, zero-padded to 6 digits.|
|`%z`|	+0000	|UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|
|`%Z`|	UTC	|Time zone name (empty string if the object is naive).|
|`%j`|	251	|Day of the year as a zero-padded decimal number.|
|`%-j`|	251	|Day of the year as a decimal number. (Platform specific)|
|`%U`|	36	|Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.|
|`%-U`|	36	|Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)|
|`%W`|	35	|Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.|
|`%-W`|	35	|Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)|
|`%c`|	Sun |Sep 8 07:06:05 2013	Locale’s appropriate date and time representation.|
|`%x`|	09/08/13	|Locale’s appropriate date representation.|
|`%X`|	07:06:05	|Locale’s appropriate time representation.|
|`%%`	|%|	A literal '%' character.|
