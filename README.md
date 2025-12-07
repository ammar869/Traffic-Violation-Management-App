1. Secure Login System

Implement password hashing (bcrypt or hashlib) to safely store & verify passwords.

Build a Tkinter login UI that checks credentials against your database securely.

2. Role-Based Navigation

After login, route users to different panels based on their role (admin, police, user).

Design separate UI frames for each panel with role-specific features.

3. Core Functionalities by Role

Admin: Manage users, officers, violation types, reports.

Police: Log violations, view assigned cases, update statuses.

User: View own violations, pay fines, appeal violations.

4. Modularize Codebase

Organize your code into clean modules: DB access, UI components, business logic.

Use classes and functions that you can reuse and maintain easily.

5. Incremental Testing

After each feature, test thoroughly with sample data.

Make sure DB reads/writes are accurate and UI responds correctly.

6. Polish & Extras

Add features like search, filters, notifications.

Improve UX with validation, error handling, and neat layouts.



| Role    | Username | Plain Password | Notes          |
| ------- | -------- | -------------- | -------------- |
| admin   | admin    | admin123       | SHA-256 hashed |
| officer | officer1 | officer123     | SHA-256 hashed |
| officer | officer2 | officer123     | SHA-256 hashed |
| user    | user1    | user123        | SHA-256 hashed |
| user    | user2    | user123        | SHA-256 hashed |


(DB project) PS C:\Users\Ammar\Documents\DB project> cd "C:\Users\Ammar\Documents\DB project"
>> python -u "app\login_gui.py"
>>