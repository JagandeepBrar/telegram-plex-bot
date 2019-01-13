# CONFIGURATION & DATABASE FILES
CONFIG_FILE = "config.ini"
DB_FILE = "database.db"

# USER ACCESSES
USER_ACCESS_ADMIN = 0
USER_ACCESS_UNVERIFIED = 1
USER_ACCESS_VERIFIED = 2
USER_ACCESS_RESTRICTED = 3
USER_ACCESS_BANNED = 4
USER_ACCESSES = [USER_ACCESS_ADMIN, USER_ACCESS_UNVERIFIED, USER_ACCESS_VERIFIED, USER_ACCESS_RESTRICTED, USER_ACCESS_BANNED]

# USER STATUSES
STATUS_ADMIN = "*You are registered as an admin/owner!*\n\nYou have full access to all commands, type /help to see all available commands."
STATUS_PENDING = "*You are registered!*\n\nYour account is pending verification, you will be notified when verification is complete."
STATUS_VERIFIED = "*You are registered and verified!*\n\nType /help to see all available commands."
STATUS_RESTRICTED = "*You are registered and verified!*\n\nYour account is active, but restricted. Please inquire with the admin(s)."
STATUS_BANNED = "*You are banned!*\n\nPlease inquire with the admins(s)."
STATUSES = [STATUS_ADMIN, STATUS_PENDING, STATUS_VERIFIED, STATUS_RESTRICTED, STATUS_BANNED]