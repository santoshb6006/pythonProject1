# Disctionary is nothing but key value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
for i in monthConversions:
    print(i)
    print("The full form of month",i,"is",monthConversions[i])
    print(f"The full form of month {i} is {monthConversions[i]}")