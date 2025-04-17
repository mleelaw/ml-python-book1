subscribers = set()
unsubscribers = set()


def add_email(email, set_name):
    set_name.add(email)


def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(
            f"Email '{email}' removed from {'subscribers' if set_name == subscribers else 'unsubscribers'}"
        )
    else:
        print(
            f"Email '{email}' not in {'subscribers' if set_name == subscribers else 'unsubscribers'}"
        )


def display_emails(set_name):
    if set_name == subscribers:
        print("All Subscriber:")
    else:
        print("All Unsubscribers:")
    for each_email in set_name:
        print(f"{each_email}")


def find_active_subscribers():
    return subscribers.difference(unsubscribers)


# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)


display_emails(subscribers)
display_emails(unsubscribers)


active_subscribers = find_active_subscribers()
print("Active Subscribers")
for email in active_subscribers:
    print(f"{email}")
