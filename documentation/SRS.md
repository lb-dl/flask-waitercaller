# Waitercaller

### Vision
Waitercaller is the web-application which notifies the waiter that their attention is wanted. When the customer wants 
service, they follow a short link or scan the QR-code which are relevant to their table, using their smartphones.
The waiter sees a notification appered on the centralized screen. The waiter then will acknowledge the notification
on the screen and attend to the client.

### Application should provide:
- Storing the account information of all the individual restaurants and available tables in a database;
- Storing the requests which are made by the restaurant's clients in the database; 
- Display a list of available tables;
- Updating the list of tables (adding, editing, removing);
- Display list of URLs which are relevant to the tables;
- Display a list of requests;
- Updating the list of requests (adding, removing);
- Updating the list of restaurants(adding);
- Saving QR-codes which are relevant to the tables;
- Display the notification.

1. Restaurants
   <br>
   <br>
    1.1 User account control  
<br>
    The application allows multiple, unrelated restaurants to use the same app. That is why, each restaurant should have
   a private login account for the system. 
<br>

- Application displays form for registration;
- User enters email, password, password conformation and presses “Submit” button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If the user with the email is already exist, then error message is displaying;
- If entered data is valid, then email and hashed password are adding to database;
- If data is added to database, the pop-up window displays a message "Sign in";
- Application displays "Sign in" form;
- User enters email and password and presses "Sign in" button;
- If entered data is valid, the "Account" page is shown;
- If any data is entered incorrectly, incorrect data messages are displayed.  
    <br>
    1.2 Managing the restaurants tables
  <br>
  <br>
   On the "Account" page restaurants can manage their tables and view the URLs that they need to make
available on the tables.
  <br>
- The application shows an input box;
- User enters the name or number of a new table in order to create it;
- When a new table is created, we'll create a unique ID number;
- When a unique ID number is created, we'll create a a new URL;
- The bitly API is used to create a shortened version of the URL;
- If entered data is valid, we store the table name, ID, and shortened URL in the database;
- If error occurs, then error message is displaying;
- When the shorten URL is created, we create a QR-code which is relevant to the table;
- The QR-code is saved into to "static" directory;
- If the data is saved in the database the page is displaying the table number (user chosen), the URL, 
      and a delete button for each table;
- If the user press "Delete" button the table name, ID, and shortened URL are removed from the database.
<br>
<br>
2. Clients
<br>
<br>
  2.1 Managing attention requests
<br>
<br>
- When a client visits the URL or scan QR-code, the table ID and the current time are saved into the database;
- Application displays a message to the client notifying them that the request was successfully made;
- If the client visits the same attention request URL repeatedly without resolving the request, the message 
  "There is already a request waiting for this table. A waiter will be there ASAP" is displayed;
- When the restaurant manager or waiter opens the dashboard of the app, they see all current attention requests
  along with the time when the request was made;
- Every attention request has a "Resolve" button;
- If the waiter has dealt with the request, they press the "Resolve" button;
- If the "Resolve" button is pressed, the table ID and the current time are deleted from the database;
- If no attention requests exist, the message "All your customers are currently satisfied - no requests" is displayed;
- The dashboard page refresh every 10 seconds, and the wait times update.
