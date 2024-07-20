#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template should be a string")
        return 
    if not isinstance(attendees, list):
        print("Error: attendees should be a list")
        return
    if not all(isinstance(d, dict) for d in attendees):
        print("Error: attendees should be a list of dictionaries")
        return
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    i = 1

    for attendee in attendees:
        processed_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = ""
            to_replace = "{" + key + "}"

            if key not in attendee:
                value = "N/A"
            else:
                value = attendee[key]

            if value == "" or value is None:
                value = "N/A"

            processed_template = processed_template.replace(to_replace, value)

        f = open("output_" + str(i) + ".txt", "a")
        f.write(processed_template)
        f.close()

        i += 1