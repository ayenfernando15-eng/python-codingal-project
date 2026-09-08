name = input("Enter the club member name: ")
club = input("Enter the school club name: ")

member_number = 12345
points = 95.5
event_count = 8
meeting_hours = 12.5
active_status = True

print("Member name:", name, "->", type(name))
print("Club name:", club, "->", type(club))
print("Member number:", member_number, "->", type(member_number))
print("Points:", points, "->", type(points))
print("Event count:", event_count, "->", type(event_count))
print("Meeting hours:", meeting_hours, "->", type(meeting_hours))
print("Active status:", active_status, "->", type(active_status))

member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points)
active_status_text = str(active_status)

badge_code = name[0:3] + name[-1:]
secret_club_code = club[::-1]

