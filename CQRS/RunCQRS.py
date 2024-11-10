from InMemoryDB import InMemoryDB
from UserCommandHandler import UserCommandHandler
from UserQueryHandler import UserQueryHandler
from Commands.CreateUserCommand import CreateUserCommand
from Commands.UpdateUserCommand import UpdateUserCommand

def main():
    db = InMemoryDB()
    user_command_handler = UserCommandHandler(db=db)
    user_query_handler = UserQueryHandler(db=db)

    # Create a new user
    create_command = CreateUserCommand(name="Vipul", email="Vipulm124@gmail.com")
    user_id = user_command_handler.handle_create_user(create_command)

    print(f"User created with id: {user_id}")

    # Fetch the created user
    user = user_query_handler.get_user_by_id(user_id=user_id)

    if user:
        print(f"Queried User: {user.user_id} | {user.name} | {user.email}")

    # Update the user
    update_command = UpdateUserCommand(user_id=user_id, name="Vipul Malhotra")
    user_command_handler.handle_update_user(command=update_command)


    # Fetch all users
    users = user_query_handler.list_users()

    for user in users:
        print(f"Listed User: {user.user_id} | {user.name} | {user.email}")


if __name__ == "__main__":
    main()