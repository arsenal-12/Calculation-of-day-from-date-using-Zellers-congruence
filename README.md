# Calculation-of-day-from-date-using-Zellers-congruence
Calculation of day from date using Zellers congruence.
Zeller's Congruence is a mathematical formula used to determine the day of the week for a given date in the Gregorian calendar. It was developed by Christian Zeller in the 19th century as a way to calculate the day of the week without relying on a computer or complex calculations. The below formula is based on modular arithmetic and involves a series of simple calculations.

 day_of_week = (day + 13*(month+1) // 5 + k + k//4 + j//4 + 5*j) % 7

1."day" represents the day of the month for the date you want to find the day of the week for.

2."month" has already been adjusted to account for January and February, where January becomes month 13 of the previous year, and February becomes month 14 of the previous year.

3."k" represents the year within the century. It is obtained by taking the last two digits of the year.

4."j" represents the zero-based century. It is obtained by taking the first two digits of the year.
