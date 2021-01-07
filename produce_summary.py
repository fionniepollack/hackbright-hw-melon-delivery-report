def print_melon_delivery_report(melon_report_filename, day):
    """The function parses the melon delivery report and prints the report for a given day."""

    melon_report_file = open(melon_report_filename)

    print("Day {}".format(day))

    # loop over each line in the file
    for line in melon_report_file:
        # remove trailing white space from line
        line = line.rstrip()
        # tokenize line at pipe
        # ex: ["Ali Baba Watermelon","18", "25.00"]
        words = line.split('|')

        # set variables based on index in array
        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))

    # close file
    melon_report_file.close()

# set cooresponding filename and day in a list of dictionary elements
reports = [
           {"filename": "um-deliveries-20140519.txt", "day": 1}, 
           {"filename": "um-deliveries-20140520.txt", "day": 2},
           {"filename": "um-deliveries-20140521.txt", "day": 3}
          ]

# loop over reports and invoke the function to print the contents
for report in reports:
    print("Filename is {} and Day is {}".format(report['filename'], report['day']))

    print_melon_delivery_report(report['filename'], report['day'])